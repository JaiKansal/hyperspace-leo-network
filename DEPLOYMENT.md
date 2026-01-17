# 🚀 HyperSpace LEO Satellite Network - Deployment Guide

## Quick Deploy (5 Minutes)

### Option 1: Render.com (Recommended - FREE)

#### Backend Deployment:

1. **Create GitHub Repository**
   ```bash
   cd "/Users/jai/Desktop/HyperSpace Innovation Hackathon."
   git init
   git add .
   git commit -m "Initial commit - HyperSpace LEO Network"
   ```

2. **Push to GitHub**
   - Go to https://github.com/new
   - Create a new repository (e.g., "hyperspace-leo-network")
   - Run:
   ```bash
   git remote add origin https://github.com/YOUR_USERNAME/hyperspace-leo-network.git
   git branch -M main
   git push -u origin main
   ```

3. **Deploy Backend on Render**
   - Go to https://render.com (sign up with GitHub)
   - Click "New +" → "Web Service"
   - Connect your GitHub repository
   - Settings:
     - **Name**: hyperspace-backend
     - **Environment**: Python 3
     - **Build Command**: `pip install -r requirements.txt`
     - **Start Command**: `uvicorn main:app --host 0.0.0.0 --port $PORT`
   - Click "Create Web Service"
   - Wait 2-3 minutes for deployment
   - Copy your backend URL (e.g., `https://hyperspace-backend.onrender.com`)

4. **Deploy Frontend on Render**
   - Click "New +" → "Static Site"
   - Connect same repository
   - Settings:
     - **Name**: hyperspace-frontend
     - **Build Command**: (leave empty)
     - **Publish Directory**: `.`
   - Click "Create Static Site"
   - Before deploying, update `globe.html` line 96 with your backend URL

#### Update Frontend to Use Deployed Backend:

Edit `globe.html` line 96:
```javascript
const API = 'https://YOUR-BACKEND-URL.onrender.com';
```

Then commit and push:
```bash
git add globe.html
git commit -m "Update API endpoint"
git push
```

---

### Option 2: Vercel (Frontend) + Railway (Backend)

#### Backend on Railway:

1. Go to https://railway.app
2. Sign in with GitHub
3. "New Project" → "Deploy from GitHub repo"
4. Select your repository
5. Railway auto-detects Python
6. Add environment variable if needed
7. Copy your backend URL

#### Frontend on Vercel:

1. Go to https://vercel.com
2. "Add New" → "Project"
3. Import your GitHub repository
4. Framework Preset: "Other"
5. Root Directory: `.`
6. Deploy!

---

### Option 3: PythonAnywhere (All-in-One - FREE)

1. Go to https://www.pythonanywhere.com
2. Sign up for free account
3. Upload your files via "Files" tab
4. Create a new web app (Flask/Django → Manual Configuration → Python 3.10)
5. Edit WSGI file to point to your FastAPI app
6. Install dependencies in Bash console:
   ```bash
   pip install --user -r requirements.txt
   ```
7. Reload web app
8. Your app will be at: `https://YOUR_USERNAME.pythonanywhere.com`

---

## 📝 Files Created for Deployment

✅ `requirements.txt` - Python dependencies
✅ `Procfile` - Tells hosting service how to run the app

---

## 🌐 Final URLs

After deployment, you'll have:
- **Backend API**: `https://your-backend.onrender.com`
- **Frontend App**: `https://your-frontend.onrender.com`

Anyone can access the frontend URL and use the app!

---

## 💡 Pro Tips

1. **Free Tier Limitations**:
   - Render free tier: Backend sleeps after 15 min of inactivity (takes 30s to wake up)
   - Solution: Use a service like UptimeRobot to ping your backend every 10 minutes

2. **Custom Domain** (Optional):
   - Buy a domain from Namecheap/GoDaddy
   - Point it to your Render/Vercel deployment
   - Example: `hyperspace.yourdomain.com`

3. **Environment Variables**:
   - If you add API keys later, use Render's environment variables feature

---

## 🚨 Quick Start (Fastest Method)

If you want to deploy RIGHT NOW:

1. Create account on Render.com
2. Click "New +" → "Web Service"
3. Choose "Public Git Repository"
4. Paste your GitHub repo URL
5. Done! (No git setup needed if repo is public)

---

## Need Help?

- Render Docs: https://render.com/docs
- Railway Docs: https://docs.railway.app
- Vercel Docs: https://vercel.com/docs
