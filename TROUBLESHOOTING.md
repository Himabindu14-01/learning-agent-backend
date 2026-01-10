# Dashboard Connection Troubleshooting Guide

## Issues Fixed

### ✅ 1. Wrong API Endpoint
**Problem:** Dashboard was calling `/latest-action/{student_id}` instead of `/plan/{student_id}`
**Fix:** Updated dashboard to use the correct `/plan/{student_id}` endpoint

### ✅ 2. Incorrect Response Handling
**Problem:** Code was treating response as an array when it's an object
**Fix:** Fixed response handling to properly access object properties

### ✅ 3. Broken Activity History Code
**Problem:** Activity history rendering had variable name conflicts and incorrect logic
**Fix:** Rewrote activity history rendering with proper logic

### ✅ 4. Better Error Handling
**Problem:** Limited error visibility
**Fix:** Added console logging and better error messages

## Testing Steps

1. **Check Backend is Running:**
   ```bash
   # Test backend directly
   curl https://learning-agent-backend.onrender.com/
   ```
   Should return: `{"status":"backend running with database"}`

2. **Check CORS:**
   - Open browser DevTools (F12)
   - Go to Network tab
   - Try loading dashboard
   - Check for CORS errors in console

3. **Check Student ID:**
   - Open browser DevTools (F12)
   - Go to Application tab > Local Storage
   - Verify `student_id` exists

4. **Check API Calls:**
   - Open browser DevTools (F12)
   - Go to Console tab
   - Look for log messages like:
     - `Making API request to: https://...`
     - `API Response: {...}`
     - `API Error: {...}`

## Common Issues

### Issue: "Network error: Could not connect to backend"
**Causes:**
- Backend URL is incorrect
- Backend is not deployed/running
- Firewall blocking requests

**Solutions:**
1. Verify backend URL in `frontend/script.js` line 11
2. Test backend URL in browser: `https://learning-agent-backend.onrender.com/`
3. Check Render dashboard to ensure service is running

### Issue: "CORS policy" error
**Causes:**
- Backend CORS not configured properly
- Frontend and backend on different domains without CORS setup

**Solutions:**
1. Verify CORS middleware in `main.py` (lines 18-24)
2. For production, update CORS to allow your frontend domain:
   ```python
   allow_origins=["https://your-frontend.vercel.app"]
   ```

### Issue: "No student profile found"
**Causes:**
- Student ID not in localStorage
- Student ID format mismatch

**Solutions:**
1. Complete onboarding flow first
2. Check localStorage in DevTools > Application > Local Storage
3. Verify student_id format matches database (UUID vs integer)

### Issue: Dashboard shows "PENDING" action
**Causes:**
- No activity_log entries for student
- Database tables not populated

**Solutions:**
1. Create activity_log entry using `/log-action` endpoint
2. Check Supabase database has data in `activity_log` table
3. Verify `student_id` in activity_log matches localStorage student_id

## Backend Endpoints Summary

- `GET /` - Health check
- `POST /student` - Create student (returns student data with ID)
- `POST /diagnostic/submit` - Submit diagnostic answers
- `GET /plan/{student_id}` - Get full dashboard data
- `GET /mastery/{student_id}` - Get mastery scores
- `POST /log-action` - Log agent decision
- `GET /latest-action/{student_id}` - Get latest action only

## Database Requirements

Ensure these Supabase tables exist:
1. **students** - with `id` (primary key, UUID)
2. **activity_log** - with `student_id`, `action`, `result`, `created_at`
3. **mastery** - with `student_id`, `topic`, `score`
4. **diagnostic_answers** - with `student_id`, `question_id`, `answer`

## Debug Checklist

- [ ] Backend URL is correct in `frontend/script.js`
- [ ] Backend is deployed and accessible
- [ ] CORS is enabled in backend
- [ ] Student ID exists in localStorage
- [ ] Browser console shows API request logs
- [ ] Database tables exist and have correct schema
- [ ] Database has data for the student_id
