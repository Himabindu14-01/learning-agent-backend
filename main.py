from fastapi import FastAPI
from pydantic import BaseModel
from supabase import create_client

# --------- SUPABASE CONFIG ----------
SUPABASE_URL = "https://ytgooccgwubohzybxrrd.supabase.co"
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Inl0Z29vY2Nnd3Vib2h6eWJ4cnJkIiwicm9sZSI6ImFub24iLCJpYXQiOjE3Njc3OTM5MzIsImV4cCI6MjA4MzM2OTkzMn0.RE53xTOx07iwVC38Txi5697TolGg_qOK0TqpmD7J1LU"

supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

# -----------------------------------

app = FastAPI()

class Student(BaseModel):
    name: str
    class_level: str
    subject: str
    goal: str
    language: str
    daily_time: int

@app.get("/")
def home():
    return {"status": "backend running with database"}

@app.post("/student")
def create_student(student: Student):
    data = supabase.table("students").insert(student.dict()).execute()
    return {"message": "Student saved to database", "data": data.data}

@app.get("/mastery/{student_id}")
def get_mastery(student_id: str):
    data = supabase.table("mastery").select("*").eq("student_id",student_id).execute()
    return data.data

@app.post("/log-action")
def log_action(payload: dict):
    supabase.table("activity_log").insert({
        "student_id": payload["student_id"],
        "action": payload["action"],
        "result": payload["result"]
    }).execute()
    return {"status": "Agent decision saved"}

@app.get("/latest-action/{student_id}")
def get_latest_action(student_id: str):
    data = supabase.table("activity_log") \
        .select("*") \
        .eq("student_id", student_id) \
        .order("created_at", desc=True) \
        .limit(1) \
        .execute()
    return data.data

