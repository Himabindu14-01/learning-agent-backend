# 🚀 Quick Start Guide

## Option 1: Run Everything Locally (Recommended for Development)

### Backend Setup
```bash
# 1. Install dependencies
pip install -r requirements.txt

# 2. Update frontend to use local backend
# Open frontend/script.js and change line 11 to:
# const API_BASE = "http://localhost:8000";

# 3. Start backend (Terminal 1)
uvicorn main:app --reload --port 8000
```

### Frontend Setup
```bash
# 4. In a NEW terminal, start frontend (Terminal 2)
cd frontend
python -m http.server 8001
```

### Access
- Frontend: http://localhost:8001/index.html
- Backend API: http://localhost:8000
- API Docs: http://localhost:8000/docs

---

## Option 2: Use Production Backend (Backend on Render)

### Frontend Only Setup
```bash
# 1. Navigate to frontend directory
cd frontend

# 2. Start frontend server
python -m http.server 8001
```

### Access
- Frontend: http://localhost:8001/index.html
- Backend: https://learning-agent-backend.onrender.com (already configured)

**Note:** Frontend is already configured to use your Render backend URL.

---

## 🎯 Step-by-Step Commands

### For Local Development:

**Terminal 1 (Backend):**
```bash
# Install dependencies (first time only)
pip install -r requirements.txt

# Start backend
uvicorn main:app --reload --port 8000
```

**Terminal 2 (Frontend):**
```bash
# Navigate to frontend
cd frontend

# Update API URL for local development (one time)
# Edit frontend/script.js line 11:
# Change to: const API_BASE = "http://localhost:8000";

# Start frontend server
python -m http.server 8001
```

**Browser:**
```
Open: http://localhost:8001/index.html
```

---

## ⚡ One-Line Commands

**Windows (PowerShell):**
```powershell
# Backend
python -m pip install -r requirements.txt; uvicorn main:app --reload --port 8000

# Frontend (new terminal)
cd frontend; python -m http.server 8001
```

**Mac/Linux:**
```bash
# Backend
pip install -r requirements.txt && uvicorn main:app --reload --port 8000

# Frontend (new terminal)
cd frontend && python -m http.server 8001
```

---

## ✅ Verification Checklist

- [ ] Backend shows: `INFO: Application startup complete`
- [ ] Frontend server is running on port 8001
- [ ] Browser opens `http://localhost:8001/index.html` without errors
- [ ] Can see onboarding form
- [ ] Browser console (F12) shows no errors

---

## 🆘 Quick Troubleshooting

| Problem | Solution |
|---------|----------|
| `pip: command not found` | Use `python -m pip` or `python3 -m pip` |
| Port 8000 in use | Change port: `--port 8001` |
| Module not found | Run `pip install -r requirements.txt` |
| CORS errors | Make sure backend is running first |
| Frontend won't load | Check you're in `frontend/` directory when running server |

---

**For detailed instructions, see `README.md`**
