from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from supabase import create_client
from typing import List, Dict, Optional
from fastapi.middleware.cors import CORSMiddleware
app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],   # Allow all origins (safe for development)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



# --------- SUPABASE CONFIG ----------
SUPABASE_URL = "https://ytgooccgwubohzybxrrd.supabase.co"
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Inl0Z29vY2Nnd3Vib2h6eWJ4cnJkIiwicm9sZSI6ImFub24iLCJpYXQiOjE3Njc3OTM5MzIsImV4cCI6MjA4MzM2OTkzMn0.RE53xTOx07iwVC38Txi5697TolGg_qOK0TqpmD7J1LU"

supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

# -----------------------------------

app = FastAPI()

# Enable CORS for frontend (production-ready)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins - Vercel frontend will work
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE", "OPTIONS"],
    allow_headers=["*"],
)

class Student(BaseModel):
    name: str
    class_level: str
    subject: str
    goal: str
    language: str
    daily_time: int

class DiagnosticSubmission(BaseModel):
    student_id: str
    answers: List[Dict]

@app.get("/")
def home():
    return {"status": "backend running with database"}

@app.post("/student")
def create_student(student: Student):
    try:
        data = supabase.table("students").insert(student.dict()).execute()
        if data.data and len(data.data) > 0:
            return {"message": "Student saved to database", "data": data.data}
        else:
            return {"message": "Student saved", "data": []}
    except Exception as e:
        return {"error": str(e)}

@app.post("/diagnostic/submit")
def submit_diagnostic(submission: DiagnosticSubmission):
    try:
        # Save diagnostic answers to database
        for answer in submission.answers:
            supabase.table("diagnostic_answers").insert({
                "student_id": submission.student_id,
                "question_id": answer.get("question_id"),
                "answer": answer.get("answer")
            }).execute()
        
        return {"message": "Diagnostic submitted successfully", "status": "success"}
    except Exception as e:
        return {"error": str(e)}

@app.get("/plan/{student_id}")
def get_plan(student_id: str):
    try:
        # Get student data - try both "id" and "student_id" columns
        student = None
        try:
            student_data = supabase.table("students").select("*").eq("id", student_id).execute()
            if student_data.data and len(student_data.data) > 0:
                student = student_data.data[0]
        except:
            try:
                student_data = supabase.table("students").select("*").eq("student_id", student_id).execute()
                if student_data.data and len(student_data.data) > 0:
                    student = student_data.data[0]
            except:
                pass
        
        # Get latest action - try to order by created_at descending
        latest_action = None
        try:
            # Try with desc=True first (if supported)
            latest_action_data = supabase.table("activity_log") \
                .select("*") \
                .eq("student_id", student_id) \
                .limit(100) \
                .execute()
            
            if latest_action_data.data and len(latest_action_data.data) > 0:
                # Sort by created_at manually to get latest
                sorted_actions = sorted(
                    latest_action_data.data,
                    key=lambda x: x.get("created_at", ""),
                    reverse=True
                )
                latest_action = sorted_actions[0] if sorted_actions else None
        except Exception as e:
            print(f"Error getting latest action: {e}")
        
        # Get mastery scores
        mastery = []
        try:
            mastery_data = supabase.table("mastery") \
                .select("*") \
                .eq("student_id", student_id) \
                .execute()
            
            if mastery_data.data:
                mastery = [{"topic": m.get("topic", "Unknown"), "score": int(m.get("score", 0))} for m in mastery_data.data]
        except Exception as e:
            print(f"Error getting mastery: {e}")
        
        # Get activity history
        activity = []
        try:
            activity_data = supabase.table("activity_log") \
                .select("*") \
                .eq("student_id", student_id) \
                .limit(10) \
                .execute()
            
            if activity_data.data:
                # Sort by created_at to get latest first
                sorted_activities = sorted(
                    activity_data.data,
                    key=lambda x: x.get("created_at", ""),
                    reverse=True
                )
                activity = [
                    f"{a.get('action', 'Unknown')}: {str(a.get('result', 'No details'))}"
                    for a in sorted_activities[:10]
                ]
        except Exception as e:
            print(f"Error getting activity: {e}")
        
        # Extract current topic and task from latest action
        current_topic = "Not assigned yet"
        task = "No task assigned yet"
        
        if latest_action:
            result = latest_action.get("result")
            if isinstance(result, dict):
                current_topic = result.get("topic", "Not assigned yet")
                task = result.get("task", "No task assigned yet")
            elif isinstance(result, str):
                task = result
                current_topic = latest_action.get("topic", "Not assigned yet")
        
        # Build response matching frontend expectations
        response = {
            "student": student,
            "current_topic": current_topic,
            "action": latest_action.get("action", "PENDING") if latest_action else "PENDING",
            "task": task,
            "mastery": mastery,
            "activity": activity
        }
        
        return response
    except Exception as e:
        import traceback
        error_detail = traceback.format_exc()
        print(f"Error in get_plan: {error_detail}")
        return {"error": str(e)}

@app.get("/mastery/{student_id}")
def get_mastery(student_id: str):
    try:
        data = supabase.table("mastery").select("*").eq("student_id", student_id).execute()
        return data.data
    except Exception as e:
        return {"error": str(e)}

@app.post("/log-action")
def log_action(payload: dict):
    try:
        supabase.table("activity_log").insert({
            "student_id": payload["student_id"],
            "action": payload["action"],
            "result": payload["result"]
        }).execute()
        return {"status": "Agent decision saved"}
    except Exception as e:
        return {"error": str(e)}

@app.get("/latest-action/{student_id}")
def get_latest_action(student_id: str):
    try:
        # Get all activity logs for this student
        data = supabase.table("activity_log") \
            .select("*") \
            .eq("student_id", student_id) \
            .limit(100) \
            .execute()
        
        if data.data and len(data.data) > 0:
            # Sort by created_at to get the most recent
            sorted_data = sorted(
                data.data,
                key=lambda x: x.get("created_at", ""),
                reverse=True
            )
            return sorted_data[0]
        
        # Return empty response instead of None to avoid JSON serialization issues
        return {
            "action": None,
            "result": None,
            "student_id": student_id,
            "message": "No action found for this student yet. Please trigger the Relay workflow."
        }
    except Exception as e:
        import traceback
        error_detail = traceback.format_exc()
        print(f"Error in get_latest_action: {error_detail}")
        return {
            "error": str(e),
            "student_id": student_id,
            "message": "Failed to fetch latest action"
        }


