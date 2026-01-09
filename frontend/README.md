# Frontend - Adaptive Learning Path Agent

Minimal, production-ready frontend for the Adaptive Learning Path Agent system.

## Structure

```
frontend/
 ├── index.html        # Student onboarding page
 ├── diagnostic.html   # Diagnostic test page
 ├── dashboard.html    # Agent dashboard (displays agent decisions)
 ├── style.css         # Shared styles
 ├── script.js         # API integration utilities
 └── README.md         # This file
```

## Setup

1. **Update Backend URL**

   Open `script.js` and update the `API_BASE` constant:

   ```javascript
   const API_BASE = "https://YOUR-BACKEND-URL.onrender.com";
   ```

   Replace `YOUR-BACKEND-URL` with your actual Render backend URL.

2. **Local Development**

   You can serve the frontend locally using any static file server:

   ```bash
   # Using Python
   python -m http.server 8000

   # Using Node.js (http-server)
   npx http-server -p 8000

   # Using PHP
   php -S localhost:8000
   ```

   Then open `http://localhost:8000` in your browser.

3. **Vercel Deployment**

   - Push your code to GitHub
   - Import the repository in Vercel
   - Set the root directory to `frontend/`
   - Deploy

   Vercel will automatically detect it as a static site.

## Pages

### 1. Onboarding (`index.html`)

- Collects student information
- Submits to `POST /student`
- Stores `student_id` in localStorage
- Redirects to diagnostic page

### 2. Diagnostic (`diagnostic.html`)

- Loads diagnostic questions
- Submits answers to `POST /diagnostic/submit`
- Redirects to dashboard

### 3. Dashboard (`dashboard.html`)

- Displays agent's decisions and plan
- Fetches data from `GET /plan/{student_id}`
- Shows:
  - Student profile
  - Current topic
  - Agent's action (REMEDIAL/PRACTICE/ADVANCE)
  - Today's task
  - Topic-wise mastery scores
  - Activity history

## API Integration

All API calls are handled through `script.js` using the `apiRequest()` function.

### Expected Backend Endpoints

- `POST /student` - Create student profile
- `POST /diagnostic/submit` - Submit diagnostic answers
- `GET /plan/{student_id}` - Get agent's plan and decisions

## Important Notes

- **This is NOT a chatbot UI** - it only displays what the agent has already decided
- **No AI logic in frontend** - all intelligence lives in the backend/Relay.app
- **Presentation layer only** - the frontend reflects autonomous agent decisions

## Browser Support

Modern browsers (Chrome, Firefox, Safari, Edge) with ES6+ support.
