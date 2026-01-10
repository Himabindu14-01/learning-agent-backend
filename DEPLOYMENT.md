# 🚀 Deployment Guide - Vercel Frontend

Complete guide to deploy your Adaptive Learning Agent frontend to Vercel.

## ✅ Prerequisites Checklist

- [x] Backend deployed on Render: `https://learning-agent-backend.onrender.com`
- [x] Supabase database configured
- [x] Relay.app workflow ready
- [x] Frontend code ready in `frontend/` directory
- [x] GitHub account

## 📦 Step 1: Prepare Frontend for Deployment

The frontend is already configured with:
- ✅ API_BASE set to your Render backend URL
- ✅ All endpoints correctly configured
- ✅ Production-ready code

**No changes needed** - the frontend is ready!

## 🌐 Step 2: Deploy to Vercel

### Option A: Deploy via Vercel Dashboard (Recommended)

1. **Push code to GitHub**
   ```bash
   git init
   git add .
   git commit -m "Initial commit - Adaptive Learning Agent"
   git branch -M main
   git remote add origin <your-github-repo-url>
   git push -u origin main
   ```

2. **Go to Vercel Dashboard**
   - Visit: https://vercel.com
   - Sign in with GitHub
   - Click "Add New Project"

3. **Import Your Repository**
   - Select your GitHub repository
   - Click "Import"

4. **Configure Project Settings**
   - **Root Directory:** `frontend`
   - **Framework Preset:** Other
   - **Build Command:** (leave empty)
   - **Output Directory:** (leave empty)
   - **Install Command:** (leave empty)

5. **Deploy**
   - Click "Deploy"
   - Wait for deployment to complete (~1-2 minutes)

6. **Your app is live!**
   - Vercel will provide a URL like: `https://your-app.vercel.app`
   - Test it immediately

### Option B: Deploy via Vercel CLI

```bash
# Install Vercel CLI
npm i -g vercel

# Navigate to frontend directory
cd frontend

# Deploy
vercel

# Follow prompts:
# - Set up and deploy? Y
# - Which scope? (select your account)
# - Link to existing project? N
# - Project name? (enter name or press enter)
# - Directory? ./
# - Override settings? N

# Production deployment
vercel --prod
```

## 🔧 Step 3: Configure Environment (If Needed)

The frontend uses hardcoded API URL, but if you need environment variables:

1. In Vercel Dashboard → Your Project → Settings → Environment Variables
2. Add: `VITE_API_BASE` = `https://learning-agent-backend.onrender.com`
3. Update `script.js` to use: `const API_BASE = process.env.VITE_API_BASE || "https://learning-agent-backend.onrender.com";`

**Note:** Current setup doesn't require this - API URL is already configured.

## ✅ Step 4: Test Your Deployment

### Test Checklist:

1. **Open your Vercel URL**
   ```
   https://your-app.vercel.app
   ```

2. **Test Onboarding**
   - Fill out student form
   - Submit
   - Should redirect to dashboard

3. **Test Dashboard**
   - Should load (may show "PENDING" if no Relay run yet)
   - Check browser console (F12) for errors

4. **Test Full Flow**
   - Create student → Get student_id
   - Trigger Relay workflow manually with student_id
   - Refresh dashboard → Should show agent decision

## 🔄 Step 5: Connect Relay Workflow

Your Relay workflow needs to be triggered manually:

1. **Get Student ID**
   - From browser localStorage (DevTools → Application → Local Storage)
   - Or from Supabase `students` table

2. **Trigger Relay Workflow**
   - Input: `{"student_id": "your-student-id"}`
   - Workflow will:
     - GET `/mastery/{student_id}`
     - Make decision (REMEDIAL/PRACTICE/ADVANCE)
     - Generate AI content
     - POST `/log-action` with result

3. **View Results**
   - Refresh dashboard
   - Should show agent decision and learning content

## 🐛 Troubleshooting

### Issue: CORS Errors
**Solution:** Backend CORS is already configured to allow all origins. If issues persist:
- Check Render backend is running
- Verify backend URL in frontend/script.js
- Check browser console for specific CORS errors

### Issue: 404 on Routes
**Solution:** The `vercel.json` file handles routing. If issues:
- Ensure `vercel.json` is in `frontend/` directory
- Check Vercel deployment logs

### Issue: API Calls Failing
**Solution:**
- Open browser DevTools → Network tab
- Check API request URL
- Verify backend is accessible: `https://learning-agent-backend.onrender.com/`
- Check backend logs on Render dashboard

### Issue: Dashboard Shows "PENDING"
**Solution:** This is normal if Relay workflow hasn't run yet:
1. Get student_id from localStorage or database
2. Trigger Relay workflow manually
3. Refresh dashboard

## 📊 Monitoring

### Vercel Analytics (Optional)
- Enable in Vercel Dashboard → Analytics
- Track page views and performance

### Error Tracking
- Check Vercel Function Logs
- Check browser console (F12)
- Check Render backend logs

## 🔐 Security Notes

Current setup:
- ✅ CORS enabled on backend
- ✅ API URL is public (acceptable for this use case)
- ✅ No sensitive data in frontend

For production enhancements:
- Add rate limiting on backend
- Implement authentication if needed
- Add API key protection for backend endpoints

## 🎯 Final Checklist

Before going live, verify:

- [ ] Frontend deployed on Vercel
- [ ] Can access Vercel URL
- [ ] Onboarding form works
- [ ] Student creation works
- [ ] Dashboard loads
- [ ] Backend API accessible
- [ ] Relay workflow can be triggered
- [ ] Agent decisions display correctly

## 📝 Quick Reference

**Frontend URL:** `https://your-app.vercel.app`  
**Backend URL:** `https://learning-agent-backend.onrender.com`  
**Supabase:** Already configured  
**Relay Workflow:** Manual trigger required

## 🆘 Support

If issues occur:
1. Check Vercel deployment logs
2. Check Render backend logs
3. Check browser console (F12)
4. Verify all URLs are correct
5. Test backend endpoints directly

---

**Your application is now live and ready to use!** 🎉
