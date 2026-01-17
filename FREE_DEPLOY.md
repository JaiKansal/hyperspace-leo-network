# 🆓 100% FREE Deployment Guide - PythonAnywhere + Vercel

## Backend: PythonAnywhere (FREE Forever)

### Step 1: Sign Up
1. Go to https://www.pythonanywhere.com/registration/register/beginner/
2. Create a **FREE** account (no credit card needed)
3. Choose a username (e.g., `jaikansaldev`)

### Step 2: Upload Your Code
1. Click **"Files"** tab
2. Click **"Upload a file"**
3. Upload these files:
   - `main.py`
   - `satellite_engine.py`
   - `requirements.txt`

### Step 3: Install Dependencies
1. Click **"Consoles"** tab
2. Click **"Bash"**
3. Run these commands:
   ```bash
   pip3.10 install --user fastapi uvicorn requests skyfield networkx
   ```

### Step 4: Create Web App
1. Click **"Web"** tab
2. Click **"Add a new web app"**
3. Choose **"Manual configuration"**
4. Select **"Python 3.10"**
5. Click through the setup

### Step 5: Configure WSGI File
1. In the **"Web"** tab, click on the WSGI configuration file link
2. Delete everything and paste this:

```python
import sys
import os

# Add your project directory to the sys.path
project_home = '/home/YOUR_USERNAME'
if project_home not in sys.path:
    sys.path = [project_home] + sys.path

# Import your FastAPI app
from main import app

# This is what PythonAnywhere will use
application = app
```

3. Replace `YOUR_USERNAME` with your PythonAnywhere username
4. Click **"Save"**

### Step 6: Enable ASGI
1. Go back to **"Web"** tab
2. Scroll to **"Code"** section
3. Change **"WSGI configuration file"** to **"ASGI configuration file"**
4. Click the ASGI file link and paste:

```python
import sys
import os

project_home = '/home/YOUR_USERNAME'
if project_home not in sys.path:
    sys.path = [project_home] + sys.path

from main import app
application = app
```

### Step 7: Reload Web App
1. Scroll to top of **"Web"** tab
2. Click the big green **"Reload"** button
3. Your backend is now live at: `https://YOUR_USERNAME.pythonanywhere.com`

---

## Frontend: Vercel (FREE Forever)

### Step 1: Deploy to Vercel
1. Go to https://vercel.com/signup
2. Sign up with GitHub (FREE, no credit card)
3. Click **"Add New"** → **"Project"**
4. Import `hyperspace-leo-network` repository
5. Configure:
   - **Framework Preset**: Other
   - **Root Directory**: `./`
   - **Build Command**: (leave empty)
   - **Output Directory**: `./`
6. Click **"Deploy"**

### Step 2: Update API URL
Before deploying, update `globe.html` line 96:
```javascript
const API = 'https://YOUR_USERNAME.pythonanywhere.com';
```

Then commit and push:
```bash
git add globe.html
git commit -m "Update API to PythonAnywhere"
git push
```

### Step 3: Get Your Live URL
After deployment (1-2 minutes), Vercel gives you:
- `https://hyperspace-leo-network.vercel.app`

---

## ✅ Your Free URLs

- **Frontend**: `https://hyperspace-leo-network.vercel.app`
- **Backend**: `https://YOUR_USERNAME.pythonanywhere.com`
- **API Docs**: `https://YOUR_USERNAME.pythonanywhere.com/docs`

---

## 🎯 Alternative: GitHub Pages (Frontend Only)

If you want even simpler frontend hosting:

1. Go to your repo: https://github.com/JaiKansal/hyperspace-leo-network
2. Click **"Settings"** → **"Pages"**
3. Source: **"Deploy from a branch"**
4. Branch: **"main"** → **"/ (root)"**
5. Click **"Save"**
6. Your site will be at: `https://jaikansal.github.io/hyperspace-leo-network/globe.html`

---

## 💡 Free Tier Limits

**PythonAnywhere FREE:**
- ✅ Always on (no sleep)
- ✅ HTTPS included
- ✅ 512MB storage
- ✅ No credit card needed
- ⚠️ Limited to pythonanywhere.com domain
- ⚠️ Slower CPU (but fine for this app)

**Vercel FREE:**
- ✅ Unlimited bandwidth
- ✅ Auto HTTPS
- ✅ Custom domains
- ✅ No credit card needed
- ✅ Fast CDN

---

## 🚀 Quick Start

1. Sign up for PythonAnywhere: https://www.pythonanywhere.com/registration/register/beginner/
2. Follow backend steps above
3. Get your backend URL
4. Update `globe.html` with backend URL
5. Push to GitHub
6. Deploy to Vercel
7. Done! 🎉

---

## Need Help?
- PythonAnywhere Help: https://help.pythonanywhere.com/
- Vercel Docs: https://vercel.com/docs
