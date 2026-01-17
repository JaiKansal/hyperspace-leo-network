# 🚀 Quick Start Guide - LEO Satellite Communication Optimizer

## ⚡ 30-Second Setup

```bash
# 1. Install dependencies
pip install -r requirements.txt

# 2. Start the server
python3 main.py

# 3. Open dashboard
open dashboard.html
```

## 🎯 API Endpoints

### Get All Satellites
```bash
curl http://localhost:8000/satellites
```

### Health Check
```bash
curl http://localhost:8000/
```

### Satellite Count
```bash
curl http://localhost:8000/satellites/count
```

## 📊 Interactive Documentation
- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

## 🧪 Run Tests
```bash
python3 test_api.py
```

## 📝 Example Response
```json
[
  {
    "id": "STARLINK-1008",
    "lat": -2.916842,
    "lon": -172.966091,
    "alt": 537.16
  },
  ...
]
```

## 🔧 Troubleshooting

### Server won't start?
```bash
# Check if port 8000 is in use
lsof -i :8000

# Kill existing process
kill -9 <PID>
```

### Dashboard not loading data?
1. Ensure server is running on port 8000
2. Check browser console for CORS errors
3. Verify API is responding: `curl http://localhost:8000/`

### TLE download fails?
- The system will use cached data automatically
- Cache is valid for 6 hours
- Check internet connection for fresh data

## 📈 Performance Tips
- First request downloads 1.5 MB TLE data (~90s)
- Subsequent requests use cache (~30ms)
- Cache refreshes automatically every 6 hours
- Use auto-refresh in dashboard for live tracking

## 🎓 Key Files
- `main.py` - FastAPI application
- `satellite_engine.py` - Orbital mechanics
- `dashboard.html` - Visualization
- `test_api.py` - Test suite
- `starlink.tle` - Cached TLE data

## 💡 Pro Tips
1. Use `/satellites/count` for quick health checks
2. Enable auto-refresh in dashboard for live monitoring
3. Check logs for detailed satellite processing info
4. TLE cache updates every 6 hours automatically

## 🌟 Features at a Glance
✅ Real-time satellite tracking (100 satellites)
✅ Intelligent caching (6-hour expiry)
✅ Beautiful dashboard with live updates
✅ Comprehensive error handling
✅ Auto-generated API docs
✅ Production-ready logging

---
**Need help?** Check README.md for detailed documentation
