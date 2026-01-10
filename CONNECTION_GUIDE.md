# Frontend-Backend Connection Guide

## ✅ What's Been Configured

### Backend (FastAPI)
- ✅ CORS middleware enabled for frontend requests
- ✅ `POST /student` - Create student profile
- ✅ `POST /diagnostic/submit` - Submit diagnostic answers
- ✅ `GET /plan/{student_id}` - Get agent's plan and decisions
- ✅ `GET /mastery/{student_id}` - Get mastery scores
- ✅ `POST /log-action` - Log agent decisions
- ✅ `GET /latest-action/{student_id}` - Get latest action

### Frontend
- ✅ API base URL set to `http://localhost:8000` for development
- ✅ All pages configured to use the API endpoints
- ✅ Error handling and loading states implemented

## 🚀 How to Run

### 1. Start the Backend

```bash
# Install dependencies if needed
pip install fastapi uvicorn supabase

# Run the backend server
uvicorn main:app --reload --port 8000
```

The backend will be available at `http://localhost:8000`

### 2. Start the Frontend

```bash
# Navigate to frontend directory
cd frontend

# Serve using Python
python -m http.server 8001

# OR using Node.js
npx http-server -p 8001

# OR using PHP
php -S localhost:8001
```

The frontend will be available at `http://localhost:8001`

### 3. Test the Connection

1. Open `http://localhost:8001/index.html` in your browser
2. Fill out the onboarding form
3. Submit to create a student profile
4. Complete the diagnostic test
5. View the dashboard with agent decisions

## 📝 Database Tables Required

Make sure your Supabase database has these tables:

1. **students** - with columns:
   - `id` (uuid, primary key)
   - `name` (text)
   - `class_level` (text)
   - `subject` (text)
   - `goal` (text)
   - `language` (text)
   - `daily_time` (integer)
   - `created_at` (timestamp)

2. **diagnostic_answers** - with columns:
   - `id` (uuid, primary key)
   - `student_id` (uuid, foreign key to students)
   - `question_id` (integer)
   - `answer` (text)
   - `created_at` (timestamp)

3. **activity_log** - with columns:
   - `id` (uuid, primary key)
   - `student_id` (uuid, foreign key to students)
   - `action` (text) - e.g., "REMEDIAL", "PRACTICE", "ADVANCE"
   - `result` (text/json) - can store task, topic, etc.
   - `created_at` (timestamp)

4. **mastery** - with columns:
   - `id` (uuid, primary key)
   - `student_id` (uuid, foreign key to students)
   - `topic` (text)
   - `score` (integer, 0-100)
   - `created_at` (timestamp)

## 🔧 For Production Deployment

### Backend (Render)
1. Update CORS to allow your frontend URL:
   ```python
   allow_origins=["https://your-frontend.vercel.app"]
   ```

### Frontend (Vercel)
1. Update `frontend/script.js`:
   ```javascript
   const API_BASE = "https://your-backend.onrender.com";
   ```

## 🐛 Troubleshooting

### CORS Errors
- Make sure CORS middleware is enabled in backend
- Check that backend URL in frontend matches actual backend URL
- For production, ensure CORS allows your frontend domain

### API Connection Failed
- Verify backend is running on port 8000
- Check browser console for specific error messages
- Ensure no firewall blocking localhost:8000

### Student ID Not Found
- Check that `/student` endpoint returns data with `id` field
- Verify localStorage has `student_id` stored
- Check browser DevTools > Application > Local Storage

## 📡 API Endpoint Details

### POST /student
**Request:**
```json
{
  "name": "John Doe",
  "class_level": "10th",
  "subject": "Mathematics",
  "goal": "exam",
  "language": "English",
  "daily_time": 60
}
```

**Response:**
```json
{
  "message": "Student saved to database",
  "data": [{"id": "uuid-here", ...}]
}
```

### POST /diagnostic/submit
**Request:**
```json
{
  "student_id": "uuid-here",
  "answers": [
    {"question_id": 1, "answer": "4"},
    {"question_id": 2, "answer": "15"}
  ]
}
```

### GET /plan/{student_id}
**Response:**
```json
{
  "student": {...},
  "current_topic": "Fractions",
  "action": "REMEDIAL",
  "task": "Practice simplifying fractions...",
  "mastery": [{"topic": "Fractions", "score": 30}],
  "activity": ["REMEDIAL: Practice fractions", "PRACTICE: Review basics"]
}
```
