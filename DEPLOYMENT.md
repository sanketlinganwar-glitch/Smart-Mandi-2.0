# 🚀 Smart Mandi - Production Deployment & Hosting Guide

This project is a full-stack Python (Flask 3.x) web application with dynamic geospatial calculations, real-time APMC mandi feeds, and an AI chat assistant.

---

## ❓ Platform Selection: Can this run on GitHub Pages?

> **❌ GitHub Pages CANNOT host this project.**
>
> - **Why:** GitHub Pages only serves static HTML/CSS/JS. It does **not** run backend runtimes like Python, Node, or Ruby.
> - **What Smart Mandi needs:** Smart Mandi requires a live Python WSGI backend server (`app.py`, Gunicorn) to process:
>   1. Server-side dataset queries (85,500+ price records across Indian mandis).
>   2. Haversine distance & net-profit optimization algorithms (`/api/ranking`).
>   3. Dynamic proxying & caching of national AGMARKNET data feeds (`/api/live/*`).
>   4. Localized multi-lingual NLP chatbot (`/api/chat`).
>
> **✅ Recommended Hosting:** **Render** (Free tier Web Service) or **Railway** / **Docker**.

---

## ⚡ Option 1: Deploy on Render (Recommended Free Cloud Hosting)

Render provides a 100% free cloud web service tier with automated GitHub deployments.

### Step-by-Step Instructions:
1. **Push your code to GitHub** (see instructions below).
2. Visit [render.com](https://render.com) and sign in with your GitHub account.
3. Click **New +** in the top navigation and select **Web Service**.
4. Select your repository (`Smart-Mandi-2.0` or `Smart-Mandi-3.0`).
5. Render will automatically read the included [`render.yaml`](render.yaml). If setting up manually, enter:
   - **Name:** `smart-mandi`
   - **Region:** Any (e.g., Singapore or Frankfurt for Asia proximity)
   - **Branch:** `main`
   - **Runtime:** `Python 3`
   - **Build Command:** `pip install -r requirements.txt`
   - **Start Command:** `gunicorn --config gunicorn.conf.py app:app`
   - **Instance Type:** `Free`
   - **Health Check Path:** `/health`
6. Click **Create Web Service**.
7. Render will build the environment, install packages, and provide you with a live URL (e.g. `https://smart-mandi-xxxx.onrender.com`).

---

## 🚂 Option 2: Deploy on Railway

1. Visit [railway.app](https://railway.app) and sign in.
2. Click **New Project** > **Deploy from GitHub repo**.
3. Select this repository.
4. Railway will automatically detect [`railway.json`](railway.json) and [`Procfile`](Procfile).
5. Deployment will start automatically.

---

## 🐳 Option 3: Deploy with Docker (Any Cloud / VPS / Cloud Run)

The repository includes an optimized multi-stage [`Dockerfile`](Dockerfile).

1. Build the container image:
   ```bash
   docker build -t smart-mandi:latest .
   ```
2. Run the container:
   ```bash
   docker run -d -p 5000:5000 -e PORT=5000 --name smart-mandi smart-mandi:latest
   ```
3. Test locally at `http://localhost:5000/health`.

---

## 💻 How to Commit & Push Changes to GitHub

To sync your code and make it live on GitHub:

```bash
# 1. Check current status
git status

# 2. Add all modified and deployment configuration files
git add .

# 3. Commit the changes with a clear message
git commit -m "Configure production deployment, health check, and route fixes"

# 4. Check your configured remote repository
git remote -v

# 5. Push to GitHub (main branch)
git push origin main
```

*(Note: If you want to push to `Smart-Mandi-2.0` instead of `Smart-Mandi-3.0`, update your git remote via: `git remote set-url origin https://github.com/sanketlinganwar-glitch/Smart-Mandi-2.0.git`)*

---

## 🧪 Local Testing & Verification

### Running locally on Windows:
```powershell
# 1. Activate virtual environment
.\venv\Scripts\activate

# 2. Start the local server
python app.py
```
*Open in browser:* `http://localhost:5000`

### Automated Health & Endpoint Verification:
You can verify that all API routes and pages are functioning with the built-in health check:
- **`GET /health`**
```json
{
  "commodities_loaded": 31,
  "markets_loaded": 51,
  "prices_loaded": 85590,
  "status": "healthy",
  "timestamp": "..."
}
```
