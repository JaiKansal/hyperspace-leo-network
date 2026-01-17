"""
Satellite Engine - The Core Physics Brain
"""
import math
import random
import logging
from datetime import datetime, timedelta
from pathlib import Path
import requests
import networkx as nx
from skyfield.api import load, EarthSatellite, wgs84

logger = logging.getLogger(__name__)

# CONFIGURATION
TLE_URL = "https://celestrak.org/NORAD/elements/gp.php?GROUP=starlink&FORMAT=tle"
TLE_CACHE_FILE = "starlink.tle"
MAX_SATELLITES = 150  
SOLAR_STORM_MODE = False
WEATHER_ZONES = [] # List of active storms

def fetch_tle_data():
    """Smart caching for TLE data"""
    cache = Path(TLE_CACHE_FILE)
    if cache.exists() and (datetime.now() - datetime.fromtimestamp(cache.stat().st_mtime)) < timedelta(hours=6):
        return TLE_CACHE_FILE
    try:
        resp = requests.get(TLE_URL, timeout=10)
        with open(TLE_CACHE_FILE, 'w') as f: f.write(resp.text)
        return TLE_CACHE_FILE
    except: return TLE_CACHE_FILE if cache.exists() else None

def get_satellite_positions():
    """Calculates position + traffic load for every satellite"""
    tle = fetch_tle_data()
    if not tle: return []
    
    ts = load.timescale()
    t = ts.now()
    sats = []
    
    with open(tle, 'r') as f: lines = f.readlines()
    
    count = 0
    for i in range(0, len(lines), 3):
        if count >= MAX_SATELLITES: break
        try:
            name = lines[i].strip()
            sat = EarthSatellite(lines[i+1], lines[i+2], name, ts)
            geo = sat.at(t)
            sub = wgs84.subpoint(geo)
            
            # SIMULATE TRAFFIC (0-100%)
            # This drives the Green/Yellow/Red coloring
            load_val = random.randint(5, 95) 
            
            sats.append({
                'id': name,
                'lat': sub.latitude.degrees,
                'lon': sub.longitude.degrees,
                'alt': sub.elevation.km,
                'load': load_val
            })
            count += 1
        except: continue
    return sats

def calculate_active_links(satellites):
    """Finds all satellites with line-of-sight"""
    links = []
    coords = []
    R = 6371.0
    
    for s in satellites:
        lat, lon = math.radians(s['lat']), math.radians(s['lon'])
        r = R + s['alt']
        x = r * math.cos(lat) * math.cos(lon)
        y = r * math.cos(lat) * math.sin(lon)
        z = r * math.sin(lat)
        coords.append((s['id'], x, y, z))
        
    for i in range(len(coords)):
        for j in range(i + 1, len(coords)):
            d = math.sqrt((coords[i][1]-coords[j][1])**2 + (coords[i][2]-coords[j][2])**2 + (coords[i][3]-coords[j][3])**2)
            if d < 2500: links.append((coords[i][0], coords[j][0]))
    return links

def get_weather_penalty(lat, lon):
    """Calculates Rain Fade penalty"""
    penalty = 1.0
    for storm in WEATHER_ZONES:
        # Approx distance check
        dist = math.sqrt((lat - storm['lat'])**2 + (lon - storm['lon'])**2)
        radius_deg = storm['radius'] / 111.0
        if dist < radius_deg:
            penalty += (storm['intensity'] * 10.0) # Massive lag spike
    return penalty

def find_best_route(s_lat, s_lon, t_lat, t_lon, satellites, links):
    global SOLAR_STORM_MODE
    
    # 1. Weather Physics
    s_penalty = get_weather_penalty(s_lat, s_lon)
    t_penalty = get_weather_penalty(t_lat, t_lon)
    weather_alert = s_penalty > 1.0 or t_penalty > 1.0

    # 2. Find Nearest Entry/Exit Nodes
    def get_nearest(lat, lon):
        best, min_d = None, float('inf')
        for s in satellites:
            d = math.sqrt((s['lat']-lat)**2 + (s['lon']-lon)**2)
            if d < min_d: best, min_d = s['id'], d
        return best

    start = get_nearest(s_lat, s_lon)
    end = get_nearest(t_lat, t_lon)
    
    if not start or not end: return {"status": "error", "message": "No Coverage"}

    # 3. Build Weighted Graph
    G = nx.Graph()
    sat_map = {s['id']: s for s in satellites}
    
    valid_nodes = set()
    for s in satellites:
        # Solar Storm: Kill 20% of sats
        if SOLAR_STORM_MODE and hash(s['id']) % 5 == 0: continue
        valid_nodes.add(s['id'])
        G.add_node(s['id'])
        
    for u, v in links:
        if u in valid_nodes and v in valid_nodes:
            s1, s2 = sat_map[u], sat_map[v]
            dist = math.sqrt((s1['lat']-s2['lat'])**2 + (s1['lon']-s2['lon'])**2)
            
            # Congestion Penalty: Avoid Red Satellites
            load_factor = (s1['load'] + s2['load']) / 200.0
            weight = dist * (1 + load_factor * 3)
            
            G.add_edge(u, v, weight=weight)

    try:
        path = nx.shortest_path(G, start, end, weight='weight')
        hops = len(path) - 1
        base_latency = hops * 12
        final_latency = base_latency * s_penalty * t_penalty
        
        return {
            "status": "success",
            "path": path,
            "hops": hops,
            "latency_ms": int(final_latency),
            "weather_alert": weather_alert,
            "storm_active": SOLAR_STORM_MODE
        }
    except: return {"status": "no_path", "message": "Signal Lost"}