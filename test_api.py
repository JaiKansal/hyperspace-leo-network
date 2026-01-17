"""
Enhanced Test Script for LEO Satellite Communication Optimizer
Tests inter-satellite link calculations and network topology
"""
import requests
import json
import time
from typing import List, Dict, Tuple
from collections import Counter


API_BASE_URL = "http://localhost:8000"


def test_enhanced_satellite_endpoint():
    """Test the enhanced /satellites endpoint with links"""
    print("🛰️  Testing Enhanced Satellite Network Endpoint...")
    start_time = time.time()
    
    response = requests.get(f"{API_BASE_URL}/satellites")
    elapsed = time.time() - start_time
    
    data = response.json()
    
    print(f"✅ Retrieved data in {elapsed:.2f}s")
    print(f"   Satellites: {data['meta']['count']}")
    print(f"   Active Links: {data['meta']['link_count']}")
    print(f"   Max Link Range: {data['meta']['max_link_range_km']} km")
    print(f"   Timestamp: {data['meta']['timestamp']}")
    print()
    
    return data


def analyze_network_topology(data: Dict):
    """Analyze the satellite network topology"""
    print("🔗 Network Topology Analysis:")
    
    satellites = data['satellites']
    links = data['links']
    
    # Calculate connectivity statistics
    sat_connections = Counter()
    for link in links:
        sat_connections[link[0]] += 1
        sat_connections[link[1]] += 1
    
    # Find most connected satellites
    most_connected = sat_connections.most_common(5)
    
    print(f"   Total Network Links: {len(links)}")
    print(f"   Average Links per Satellite: {len(links) * 2 / len(satellites):.1f}")
    print()
    
    print("   Most Connected Satellites:")
    for sat_id, link_count in most_connected:
        print(f"      {sat_id:20s} - {link_count} links")
    print()
    
    # Find isolated satellites (no links)
    connected_sats = set()
    for link in links:
        connected_sats.add(link[0])
        connected_sats.add(link[1])
    
    all_sats = {sat['id'] for sat in satellites}
    isolated = all_sats - connected_sats
    
    print(f"   Connected Satellites: {len(connected_sats)}/{len(satellites)}")
    if isolated:
        print(f"   Isolated Satellites: {len(isolated)}")
        print(f"      {', '.join(list(isolated)[:5])}")
    else:
        print(f"   ✅ All satellites are connected!")
    print()


def analyze_link_distribution(data: Dict):
    """Analyze geographical distribution of links"""
    print("🌍 Link Distribution Analysis:")
    
    satellites = data['satellites']
    links = data['links']
    
    # Create satellite lookup
    sat_lookup = {sat['id']: sat for sat in satellites}
    
    # Analyze link distances and orientations
    link_distances = []
    
    for link in links[:50]:  # Sample first 50 for performance
        sat1 = sat_lookup.get(link[0])
        sat2 = sat_lookup.get(link[1])
        
        if sat1 and sat2:
            # Simple distance approximation
            lat_diff = abs(sat1['lat'] - sat2['lat'])
            lon_diff = abs(sat1['lon'] - sat2['lon'])
            link_distances.append((lat_diff, lon_diff))
    
    if link_distances:
        avg_lat_diff = sum(d[0] for d in link_distances) / len(link_distances)
        avg_lon_diff = sum(d[1] for d in link_distances) / len(link_distances)
        
        print(f"   Average Link Span (sample):")
        print(f"      Latitude: {avg_lat_diff:.1f}°")
        print(f"      Longitude: {avg_lon_diff:.1f}°")
    print()


def test_network_performance():
    """Test network update performance"""
    print("⚡ Network Performance Test:")
    
    times = []
    for i in range(5):
        start = time.time()
        response = requests.get(f"{API_BASE_URL}/satellites")
        elapsed = time.time() - start
        times.append(elapsed)
        
        if i < 4:  # Don't sleep on last iteration
            time.sleep(0.5)
    
    avg_time = sum(times) / len(times)
    min_time = min(times)
    max_time = max(times)
    
    print(f"   Average Response Time: {avg_time*1000:.1f} ms")
    print(f"   Min: {min_time*1000:.1f} ms | Max: {max_time*1000:.1f} ms")
    print()


def visualize_sample_network(data: Dict):
    """Display a sample of the network structure"""
    print("📊 Sample Network Visualization:")
    
    satellites = data['satellites'][:10]
    links = data['links'][:15]
    
    # Create satellite ID to index mapping
    sat_ids = [sat['id'] for sat in satellites]
    
    print("   Satellites:")
    for i, sat in enumerate(satellites):
        print(f"      [{i}] {sat['id']:20s} @ ({sat['lat']:6.2f}°, {sat['lon']:7.2f}°)")
    
    print("\n   Active Links:")
    for link in links:
        if link[0] in sat_ids and link[1] in sat_ids:
            idx1 = sat_ids.index(link[0])
            idx2 = sat_ids.index(link[1])
            print(f"      [{idx1}] {link[0]} <-> [{idx2}] {link[1]}")
    print()


def main():
    """Run all enhanced tests"""
    print("=" * 70)
    print("🚀 LEO Satellite Communication Optimizer - Enhanced Test Suite")
    print("   With Inter-Satellite Link Analysis")
    print("=" * 70)
    print()
    
    try:
        # Test enhanced endpoint
        data = test_enhanced_satellite_endpoint()
        
        # Analyze network topology
        analyze_network_topology(data)
        
        # Analyze link distribution
        analyze_link_distribution(data)
        
        # Test performance
        test_network_performance()
        
        # Visualize sample network
        visualize_sample_network(data)
        
        print("=" * 70)
        print("✅ All enhanced tests completed successfully!")
        print("   Open globe.html to see the 3D visualization!")
        print("=" * 70)
        
    except requests.exceptions.ConnectionError:
        print("❌ Error: Could not connect to API server")
        print("   Make sure the server is running: python3 main.py")
    except Exception as e:
        print(f"❌ Error: {str(e)}")
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    main()
