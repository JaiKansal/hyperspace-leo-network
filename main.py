"""
Main API - Handles Requests, Geocoding, and Simulation Toggles
"""
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Union, Optional
import requests
import satellite_engine as engine

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def resolve_coords(query):
    """Returns (lat, lon, display_name)"""
    try:
        val = float(query)
        return val, 0.0, f"Coords({val},{0.0})"
    except:
        try:
            url = f"https://nominatim.openstreetmap.org/search?q={query}&format=json&limit=1"
            headers = {'User-Agent': 'LEO_Hackathon_App'}
            resp = requests.get(url, headers=headers, timeout=2).json()
            if resp:
                return float(resp[0]['lat']), float(resp[0]['lon']), resp[0]['display_name'].split(',')[0]
        except: pass
    return 0.0, 0.0, "Unknown"

class LocationInput(BaseModel):
    lat: Union[str, float]
    lon: Optional[Union[str, float]] = None

class RouteRequest(BaseModel):
    source: LocationInput
    target: LocationInput

@app.get("/satellites")
async def get_satellites():
    sats = engine.get_satellite_positions()
    links = engine.calculate_active_links(sats)
    return {"satellites": sats, "links": links, "meta": {"count": len(sats), "link_count": len(links)}}

@app.post("/route")
async def calculate_route(req: RouteRequest):
    # Resolve Source
    if req.source.lon is not None:
        s_lat, s_lon = float(req.source.lat), float(req.source.lon)
        s_name = "Custom Coords"
    else:
        s_lat, s_lon, s_name = resolve_coords(req.source.lat)
        if s_name == "Unknown": s_name = str(req.source.lat)

    # Resolve Target
    if req.target.lon is not None:
        t_lat, t_lon = float(req.target.lat), float(req.target.lon)
        t_name = "Custom Coords"
    else:
        t_lat, t_lon, t_name = resolve_coords(req.target.lat)
        if t_name == "Unknown": t_name = str(req.target.lat)

    sats = engine.get_satellite_positions()
    links = engine.calculate_active_links(sats)
    
    result = engine.find_best_route(s_lat, s_lon, t_lat, t_lon, sats, links)
    
    # Add Transparency Data
    result["resolution"] = {
        "source_used": s_name,
        "source_coords": [s_lat, s_lon],
        "target_used": t_name,
        "target_coords": [t_lat, t_lon]
    }
    return result

@app.post("/toggle-weather")
async def toggle_weather():
    if not engine.WEATHER_ZONES:
        engine.WEATHER_ZONES = [{'lat': 35.0, 'lon': -40.0, 'radius': 1000, 'intensity': 0.8}]
        status = "STORMY"
    else:
        engine.WEATHER_ZONES = []
        status = "CLEAR"
    return {"status": status}

@app.post("/toggle-storm")
async def toggle_storm():
    engine.SOLAR_STORM_MODE = not engine.SOLAR_STORM_MODE
    return {"storm_active": engine.SOLAR_STORM_MODE}