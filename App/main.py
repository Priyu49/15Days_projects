from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from pathlib import Path
import json
from datetime import datetime
from App.load_records import load_records

from App.smart_search import smart_search


# Initialize FastAPI application
app = FastAPI(
    title="MindMate API",
    description="Personal Productivity Assistant API",
    version="1.0.0"
)


# Project paths
BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "Data"
QUESTIONS_FILE = DATA_DIR / "questions.json"


# Request model for submitting questions
class Question(BaseModel):
    name: str
    question: str


# 1. Home route
@app.get("/")
def home():
    return {
        "message": "Welcome to MindMate API!",
        "status": "Running"
    }


# 2. Health check API
@app.get("/health")
def health_check():
    return {
        "status": "healthy",
        "application": "MindMate"
    }


# 3. Get all productivity records
@app.get("/records")
def get_all_records():

    records = load_records()

    if not records:
        raise HTTPException(
            status_code=404,
            detail="No records found. Run the ingestion script first."
        )

    return {
        "total_records": len(records),
        "records": records
    }


# 4. Get a record using its ID
@app.get("/records/{record_id}")
def get_record_by_id(record_id: int):

    records = load_records()

    for record in records:
        if int(record["id"]) == record_id:
            return record

    raise HTTPException(
        status_code=404,
        detail="Record not found"
    )


# 5. Search productivity records
@app.get("/search")
def search_records(q: str):

    if not q.strip():
        raise HTTPException(
            status_code=400,
            detail="Please enter a search keyword"
        )

    results = smart_search(q, top_n=3)

    return {
        "search_query": q,
        "total_results": len(results),
        "results": results
    }

# 6. Submit a question
@app.post("/questions")
def submit_question(data: Question):

    DATA_DIR.mkdir(parents=True, exist_ok=True)

    if QUESTIONS_FILE.exists():
        with open(QUESTIONS_FILE, "r", encoding="utf-8") as file:
            questions = json.load(file)
    else:
        questions = []

    new_question = {
        "id": len(questions) + 1,
        "name": data.name,
        "question": data.question,
        "created_at": datetime.now().isoformat()
    }

    questions.append(new_question)

    with open(QUESTIONS_FILE, "w", encoding="utf-8") as file:
        json.dump(questions, file, indent=4)

    return {
        "message": "Question submitted successfully!",
        "data": new_question
    }
