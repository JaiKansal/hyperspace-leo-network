# 🚀 DEPLOY NOW - Step-by-Step Guide

Your code is now on GitHub! 
**Repository**: https://github.com/JaiKansal/hyperspace-leo-network

---

## 🎯 One-Click Deploy to Render (Recommended)

### Method 1: Blueprint Deploy (Easiest - 2 minutes)

1. **Click this link to deploy both backend AND frontend in one click:**
   
   [![Deploy to Render](https://render.com/images/deploy-to-render-button.svg)](https://render.com/deploy?repo=https://github.com/JaiKansal/hyperspace-leo-network)

2. **Sign in to Render** (use your GitHub account)

3. **Click "Apply"** - Render will automatically:
   - Deploy your backend API
   - Deploy your frontend
   - Set up HTTPS
   - Give you public URLs

4. **Wait 3-5 minutes** for deployment to complete

5. **Get your URLs:**
   - Backend: `https://hyperspace-backend.onrender.com`
   - Frontend: `https://hyperspace-frontend.onrender.com`

6. **Update the frontend** to use the backend URL:
   - Edit `globe.html` line 96
   - Change to: `const API = 'https://hyperspace-backend.onrender.com';`
   - Commit and push:
     ```bash
     git add globe.html
     git commit -m "Update API endpoint to production URL"
     git push
     ```

7. **Done!** Visit your frontend URL and share it with anyone!

---

## 🔧 Method 2: Manual Deploy (More Control)

### Step 1: Deploy Backend

1. Go to https://render.com/dashboard
2. Click **"New +"** → **"Web Service"**
3. Click **"Connect a repository"** → Select `hyperspace-leo-network`
4. Configure:
   - **Name**: `hyperspace-backend`
   - **Runtime**: Python 3
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `uvicorn main:app --host 0.0.0.0 --port $PORT`
   - **Plan**: Free
5. Click **"Create Web Service"**
6. Wait 2-3 minutes for deployment
7. **Copy your backend URL** (e.g., `https://hyperspace-backend-xyz.onrender.com`)

### Step 2: Update Frontend

1. Edit `globe.html` line 96:
   ```javascript
   const API = 'https://YOUR-BACKEND-URL.onrender.com';
   ```

2. Commit and push:
   ```bash
   git add globe.html
   git commit -m "Update API endpoint"
   git push
   ```

### Step 3: Deploy Frontend

1. On Render dashboard, click **"New +"** → **"Static Site"**
2. Select `hyperspace-leo-network` repository
3. Configure:
   - **Name**: `hyperspace-frontend`
   - **Build Command**: (leave empty)
   - **Publish Directory**: `.`
4. Click **"Create Static Site"**
5. Wait 1-2 minutes
6. **Copy your frontend URL** (e.g., `https://hyperspace-frontend.onrender.com`)

### Step 4: Test!

Visit your frontend URL and test all features:
- ✅ Satellite visualization
- ✅ Route calculation
- ✅ Rain storm simulation
- ✅ Solar flare simulation
- ✅ Flight simulation

---

## 🌐 Your Live URLs

After deployment, you'll have:

- **🎨 Frontend (Share this!)**: `https://hyperspace-frontend.onrender.com`
- **⚙️ Backend API**: `https://hyperspace-backend.onrender.com`
- **📚 API Docs**: `https://hyperspace-backend.onrender.com/docs`
- **📖 GitHub Repo**: https://github.com/JaiKansal/hyperspace-leo-network

---

## 📱 Share Your App

Once deployed, anyone can access your app at the frontend URL!

**Example sharing message:**
```
🛰️ Check out HyperSpace - LEO Satellite Network Optimizer!

Interactive 3D visualization of Starlink satellites with:
✨ Real-time satellite tracking
🚀 Intelligent routing algorithms
🌧️ Weather simulation (rain fade)
☀️ Solar storm simulation
✈️ Flight path tracking

Try it: https://hyperspace-frontend.onrender.com
```

---

## ⚡ Performance Notes

**Free Tier Behavior:**
- Backend sleeps after 15 minutes of inactivity
- First request after sleep takes ~30 seconds to wake up
- Subsequent requests are instant

**Solution for Always-On:**
- Use UptimeRobot.com (free) to ping your backend every 10 minutes
- Or upgrade to Render's paid plan ($7/month for always-on)

---

## 🔄 Future Updates

To update your deployed app:

1. Make changes locally
2. Commit and push:
   ```bash
   git add .
   git commit -m "Your update message"
   git push
   ```
3. Render auto-deploys in 1-2 minutes!

---

## 🆘 Troubleshooting

**Backend won't start?**
- Check Render logs for errors
- Verify `requirements.txt` has all dependencies
- Check that `Procfile` is correct

**Frontend can't reach backend?**
- Verify `globe.html` line 96 has correct backend URL
- Check browser console for CORS errors
- Ensure backend is running (visit `/docs` endpoint)

**Need help?**
- Render Docs: https://render.com/docs
- GitHub Issues: https://github.com/JaiKansal/hyperspace-leo-network/issues

---

## 🎉 You're Ready!

Click the deploy button above or follow the manual steps.
Your app will be live in under 5 minutes!

**Repository**: https://github.com/JaiKansal/hyperspace-leo-network
