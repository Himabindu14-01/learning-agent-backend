# Adaptive Learning Path Agent - Full Stack Application

A full-stack application for an adaptive learning path agent designed for rural students, with FastAPI backend and vanilla JavaScript frontend.

## 📋 Prerequisites

- **Python 3.8+** installed
- **Supabase account** (for database) - Already configured
- **Web browser** (Chrome, Firefox, Safari, or Edge)

## 🚀 Quick Start Guide

### Step 1: Install Python Dependencies

```bash
# Install required Python packages
pip install -r requirements.txt
```

Or install manually:
```bash
pip install fastapi uvicorn supabase pydantic python-multipart
```

### Step 2: Run the Backend Server

Open a terminal/command prompt in the project root directory and run:

```bash
# Development mode with auto-reload
uvicorn main:app --reload --port 8000

# Or production mode
uvicorn main:app --host 0.0.0.0 --port 8000
```

You should see output like:
```
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
INFO:     Started reloader process
INFO:     Started server process
INFO:     Waiting for application startup.
INFO:     Application startup complete.
```

**Backend will be running at:** `http://localhost:8000`

### Step 3: Run the Frontend

Open a **NEW** terminal/command prompt and navigate to the frontend directory:

```bash
# Navigate to frontend directory
cd frontend

# Option 1: Using Python (if Python 3.x is installed)
python -m http.server 8001

# Option 2: Using Node.js (if Node.js is installed)
npx http-server -p 8001

# Option 3: Using PHP (if PHP is installed)
php -S localhost:8001
```

You should see output like:
```
Serving HTTP on 0.0.0.0 port 8001 (http://0.0.0.0:8001/) ...
```

**Frontend will be running at:** `http://localhost:8001`

### Step 4: Access the Application

Open your web browser and go to:
```
http://localhost:8001/index.html
```

## 📁 Project Structure

```
learning-agent-backend/
├── main.py                 # FastAPI backend server
├── requirements.txt        # Python dependencies
├── frontend/
│   ├── index.html         # Student onboarding page
│   ├── diagnostic.html    # Diagnostic test page
│   ├── dashboard.html     # Agent dashboard
│   ├── style.css          # Styling
│   └── script.js          # API integration
└── README.md              # This file
```

## 🔧 Configuration

### Backend Configuration

The backend is already configured with:
- **Supabase URL & Key** - Configured in `main.py` (lines 8-9)
- **CORS** - Enabled for all origins (configured in `main.py` lines 18-24)

### Frontend Configuration

The frontend API URL is set in `frontend/script.js` (line 11):
```javascript
const API_BASE = "https://learning-agent-backend.onrender.com";  // Production
// For local: "http://localhost:8000"
```

**For Local Development:** Change line 11 in `frontend/script.js` to:
```javascript
const API_BASE = "http://localhost:8000";
```

## 🧪 Testing the Setup

### 1. Test Backend
Open in browser or use curl:
```bash
# Browser: http://localhost:8000/
# Or curl:
curl http://localhost:8000/
```

Expected response:
```json
{"status": "backend running with database"}
```

### 2. Test Frontend
Open in browser:
```
http://localhost:8001/index.html
```

You should see the onboarding form.

### 3. Test Full Flow
1. Fill out the onboarding form → Creates student profile
2. Complete diagnostic test → Submits answers
3. View dashboard → Shows agent decisions

## 🐛 Troubleshooting

### Backend Issues

**Problem:** `ModuleNotFoundError: No module named 'fastapi'`
```bash
pip install -r requirements.txt
```

**Problem:** Port 8000 already in use
```bash
# Use a different port
uvicorn main:app --reload --port 8001
# Then update frontend/script.js API_BASE to use port 8001
```

**Problem:** `Connection refused` errors
- Make sure backend is running first
- Check firewall settings
- Verify you're using the correct port

### Frontend Issues

**Problem:** CORS errors in browser console
- Make sure backend CORS is enabled (already configured)
- Verify backend is running on the correct port
- Check browser console for specific error messages

**Problem:** API calls failing
- Open browser DevTools (F12) → Console tab
- Check for API request logs
- Verify `API_BASE` URL in `frontend/script.js` matches your backend URL

**Problem:** Dashboard shows "No student profile found"
- Complete onboarding flow first
- Check localStorage in DevTools → Application → Local Storage
- Verify `student_id` exists

## 📡 API Endpoints

- `GET /` - Health check
- `POST /student` - Create student profile
- `POST /diagnostic/submit` - Submit diagnostic answers
- `GET /plan/{student_id}` - Get dashboard data
- `GET /mastery/{student_id}` - Get mastery scores
- `POST /log-action` - Log agent decision
- `GET /latest-action/{student_id}` - Get latest action

See API documentation at: `http://localhost:8000/docs` (when backend is running)

## 🌐 Deployment

### Backend Deployment (Render)
1. Push code to GitHub
2. Connect to Render
3. Set build command: `pip install -r requirements.txt`
4. Set start command: `uvicorn main:app --host 0.0.0.0 --port $PORT`
5. Update frontend `API_BASE` with Render URL

### Frontend Deployment (Vercel)
1. Push code to GitHub
2. Import repository in Vercel
3. Set root directory to `frontend/`
4. Deploy

## 📚 Additional Resources

- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [Supabase Documentation](https://supabase.com/docs)
- See `CONNECTION_GUIDE.md` for detailed connection setup
- See `TROUBLESHOOTING.md` for common issues and solutions

## 💡 Tips

- Keep backend terminal open while developing
- Use browser DevTools (F12) to debug frontend issues
- Check backend terminal for API request logs
- Backend auto-reloads on code changes (with `--reload` flag)

## ✅ Success Indicators

You know everything is working when:
- ✅ Backend shows "Application startup complete"
- ✅ Frontend serves on port 8001
- ✅ Browser opens onboarding form without errors
- ✅ You can create a student profile
- ✅ Dashboard loads after diagnostic test

---

**Need help?** Check `TROUBLESHOOTING.md` for common issues and solutions.
