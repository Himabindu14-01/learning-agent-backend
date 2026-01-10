# 🧪 Testing Checklist

Complete testing guide for your Adaptive Learning Agent application.

## Pre-Deployment Testing

### 1. Backend Testing

```bash
# Test backend health
curl https://learning-agent-backend.onrender.com/

# Expected: {"status":"backend running with database"}
```

**Test Endpoints:**
- [ ] `GET /` - Returns health status
- [ ] `POST /student` - Creates student (test with sample data)
- [ ] `GET /mastery/{student_id}` - Returns mastery data (test with existing ID)
- [ ] `GET /latest-action/{student_id}` - Returns latest action (test with existing ID)

### 2. Frontend Local Testing

```bash
# Start local server
cd frontend
python -m http.server 8001

# Open browser
# http://localhost:8001/index.html
```

**Test Onboarding:**
- [ ] Form validates required fields
- [ ] Submits successfully to backend
- [ ] Stores student_id in localStorage
- [ ] Redirects to dashboard

**Test Dashboard:**
- [ ] Loads without errors
- [ ] Fetches latest action from backend
- [ ] Displays "PENDING" if no action exists
- [ ] Shows error message if backend unavailable

## Post-Deployment Testing (Vercel)

### 3. Production Frontend Testing

**Test URL:** `https://your-app.vercel.app`

**Onboarding Flow:**
- [ ] Page loads correctly
- [ ] Form submission works
- [ ] Student created in database
- [ ] Redirect to dashboard works

**Dashboard Flow:**
- [ ] Dashboard loads
- [ ] Shows student information
- [ ] Fetches from correct backend URL
- [ ] Handles empty state gracefully

### 4. End-to-End Testing

**Full Workflow Test:**

1. **Create Student**
   - [ ] Fill onboarding form
   - [ ] Submit successfully
   - [ ] Note student_id from localStorage or database

2. **Trigger Relay Workflow**
   - [ ] Open Relay.app
   - [ ] Trigger workflow with `{"student_id": "your-id"}`
   - [ ] Verify workflow completes successfully
   - [ ] Check Supabase `activity_log` table has new entry

3. **View Results**
   - [ ] Refresh dashboard
   - [ ] Verify agent decision displays (REMEDIAL/PRACTICE/ADVANCE)
   - [ ] Verify learning content displays
   - [ ] Verify mastery scores display (if available)

## Integration Testing

### 5. Data Flow Testing

**Test Data Flow:**

```
Frontend → Backend → Supabase
         ↑
    Relay.app
```

- [ ] Frontend can create student (Frontend → Backend → Supabase)
- [ ] Relay can read mastery (Relay → Backend → Supabase)
- [ ] Relay can save action (Relay → Backend → Supabase)
- [ ] Frontend can read action (Frontend → Backend → Supabase)

### 6. Error Handling Testing

**Test Error Scenarios:**
- [ ] Backend down → Frontend shows error message
- [ ] Invalid student_id → Dashboard shows appropriate message
- [ ] Network error → Frontend handles gracefully
- [ ] Empty response → Dashboard shows "PENDING" state

## Browser Compatibility Testing

### 7. Cross-Browser Testing

Test in multiple browsers:
- [ ] Chrome/Edge (Chromium)
- [ ] Firefox
- [ ] Safari
- [ ] Mobile browsers (optional)

## Performance Testing

### 8. Performance Checks

- [ ] Page load time < 3 seconds
- [ ] API response time < 2 seconds
- [ ] Dashboard renders quickly
- [ ] No console errors

## Security Testing

### 9. Security Checks

- [ ] CORS working correctly
- [ ] No sensitive data in frontend code
- [ ] API calls use HTTPS
- [ ] Input validation working

## User Experience Testing

### 10. UX Testing

- [ ] Clear error messages
- [ ] Loading states visible
- [ ] Forms are intuitive
- [ ] Dashboard is readable
- [ ] Mobile responsive (if needed)

## Regression Testing

### 11. Verify Existing Features

After any changes, verify:
- [ ] Student creation still works
- [ ] Dashboard still loads
- [ ] Relay integration still works
- [ ] All endpoints still functional

## Quick Test Script

```javascript
// Run in browser console on dashboard page

async function testIntegration() {
    const studentId = localStorage.getItem('student_id');
    
    if (!studentId) {
        console.error('No student_id found');
        return;
    }
    
    console.log('Testing with student_id:', studentId);
    
    // Test latest action
    try {
        const response = await fetch(`https://learning-agent-backend.onrender.com/latest-action/${studentId}`);
        const data = await response.json();
        console.log('Latest action:', data);
    } catch (e) {
        console.error('Error fetching latest action:', e);
    }
    
    // Test mastery
    try {
        const response = await fetch(`https://learning-agent-backend.onrender.com/mastery/${studentId}`);
        const data = await response.json();
        console.log('Mastery:', data);
    } catch (e) {
        console.error('Error fetching mastery:', e);
    }
}

testIntegration();
```

## Test Results Template

```
Date: _______________
Tester: _______________

Backend Tests: [ ] Pass [ ] Fail
Frontend Tests: [ ] Pass [ ] Fail
Integration Tests: [ ] Pass [ ] Fail
E2E Tests: [ ] Pass [ ] Fail

Issues Found:
1. ___________________________
2. ___________________________

Status: [ ] Ready for Production [ ] Needs Fixes
```

---

**After completing all tests, your application is ready for production use!** ✅
