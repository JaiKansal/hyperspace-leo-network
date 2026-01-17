# 🛰️ HyperSpace - LEO Satellite Network Optimizer

An interactive 3D visualization and routing optimizer for Low Earth Orbit (LEO) satellite networks, featuring real-time Starlink satellite tracking, intelligent path optimization, and environmental hazard simulation.

![HyperSpace Demo](https://img.shields.io/badge/Status-Live-success)
![Python](https://img.shields.io/badge/Python-3.10+-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-0.104-green)

## 🌟 Features

### Real-Time Satellite Tracking
- **150 Starlink satellites** tracked in real-time using TLE data from CelesTrak
- **3D Earth visualization** powered by Cesium.js
- **Traffic heatmap**: Satellites color-coded by network load (Green → Yellow → Red)
- **Inter-satellite links** visualization (up to 150 active links)

### Intelligent Routing
- **Smart geocoding**: Type city names (e.g., "Hapur", "London") instead of coordinates
- **AI-powered path optimization**: Dijkstra's algorithm with congestion penalties
- **Load balancing**: Routes avoid high-traffic satellites
- **Real-time latency calculation**: Physics-based signal propagation modeling

### Environmental Hazards
- **🌧️ Rain Fade Simulation**: Atlantic storm zone with signal attenuation
- **☀️ Solar Storm Mode**: 20% satellite failure simulation (CME events)
- **Educational storytelling**: Pop-up explanations of real-world physics

### Flight Simulation
- **Tokyo → Sydney flight path** with dynamic satellite handover
- **Moving target routing**: Route recalculates as the plane moves
- **Visual progress tracking**

## 🚀 Live Demo

**Frontend**: [Your Deployed URL]  
**Backend API**: [Your Backend URL]

## 🛠️ Tech Stack

### Backend
- **FastAPI** - High-performance Python web framework
- **Skyfield** - Astronomical calculations for satellite positions
- **NetworkX** - Graph-based routing algorithms
- **Requests** - TLE data fetching from CelesTrak

### Frontend
- **Cesium.js** - 3D geospatial visualization
- **Vanilla JavaScript** - No framework dependencies
- **OpenStreetMap Nominatim** - Geocoding API

## 📦 Installation

### Prerequisites
- Python 3.10+
- Modern web browser (Chrome, Firefox, Safari)

### Local Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/YOUR_USERNAME/hyperspace-leo-network.git
   cd hyperspace-leo-network
   ```

2. **Install Python dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the backend**
   ```bash
   uvicorn main:app --reload --port 8000
   ```

4. **Run the frontend**
   ```bash
   python3 -m http.server 5500
   ```

5. **Open in browser**
   ```
   http://localhost:5500/globe.html
   ```

## 🌐 Deployment

See [DEPLOYMENT.md](DEPLOYMENT.md) for detailed deployment instructions to:
- Render.com (Recommended)
- Railway + Vercel
- PythonAnywhere

## 📡 API Endpoints

### `GET /satellites`
Returns current positions of all tracked satellites with inter-satellite links.

**Response:**
```json
{
  "satellites": [
    {"id": "STARLINK-1234", "lat": 40.7, "lon": -74.0, "alt": 550, "load": 45}
  ],
  "links": [["STARLINK-1234", "STARLINK-5678"]],
  "meta": {"count": 150, "link_count": 450}
}
```

### `POST /route`
Calculates optimal routing path through the satellite network.

**Request:**
```json
{
  "source": {"lat": "Hapur"},
  "target": {"lat": "London"}
}
```

**Response:**
```json
{
  "status": "success",
  "path": ["STARLINK-1234", "STARLINK-5678"],
  "hops": 5,
  "latency_ms": 87,
  "weather_alert": false,
  "resolution": {
    "source_used": "Hapur",
    "target_used": "London"
  }
}
```

### `POST /toggle-weather`
Toggles rain storm simulation over the Atlantic Ocean.

### `POST /toggle-storm`
Toggles solar storm mode (disables 20% of satellites).

## 🎓 Educational Features

The app includes real-world physics explanations:

- **Rain Fade**: How water absorbs high-frequency radio waves
- **Solar Flares**: Coronal Mass Ejections (CME) and satellite protection
- **Satellite Handover**: How moving targets maintain connectivity
- **Load Balancing**: Network congestion management

## 🏗️ Architecture

```
┌─────────────────┐
│   Frontend      │
│  (Cesium.js)    │
│   globe.html    │
└────────┬────────┘
         │ HTTPS
         ▼
┌─────────────────┐
│   Backend       │
│   (FastAPI)     │
│    main.py      │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ Satellite Engine│
│ (Skyfield +     │
│  NetworkX)      │
└─────────────────┘
```

## 🤝 Contributing

Contributions welcome! Areas for improvement:
- [ ] Add more satellite constellations (OneWeb, Kuiper)
- [ ] Implement Kalman filtering for position prediction
- [ ] Add ground station network
- [ ] Real-time satellite health monitoring
- [ ] Multi-path routing with failover

## 📄 License

MIT License - feel free to use for educational or commercial purposes.

## 🙏 Acknowledgments

- **CelesTrak** for TLE data
- **Cesium** for 3D visualization platform
- **OpenStreetMap** for geocoding services
- **Starlink** for inspiring the next generation of satellite networks

## 📧 Contact

Built for HyperSpace Innovation Hackathon 2026

---

**⭐ Star this repo if you found it useful!**
