# app.py (FastAPI server)
from fastapi import FastAPI, HTTPException, Header
from pydantic import BaseModel
from transformers import pipeline
import uvicorn
from preprocess import clean_text  # Import preprocessing function
from summarize_model import summarize_text  # Import summarization function

app = FastAPI()

# API key for security (Optional)
API_KEY = "my_secure_api_key"

# Define request model
class ReportRequest(BaseModel):
    report_text: str

@app.get("/")
def home():
    return {"message": "Welcome to the Medical Report Summarizer API!"}

@app.post("/summarize/")
def summarize(report: ReportRequest, api_key: str = Header(None)):
    """Accepts a medical report and returns a summarized version."""
   # if api_key != API_KEY:
   #     raise HTTPException(status_code=403, detail="Invalid API Key")

    if not report.report_text.strip():
        raise HTTPException(status_code=400, detail="Report text cannot be empty")

    cleaned_text = clean_text(report.report_text)  # Preprocess input
    summary = summarize_text(cleaned_text)  # Generate summary
    return {"summary": summary}

if __name__ == "__main__":
    uvicorn.run("app:app", host="127.0.0.1", port=8000, reload=True)