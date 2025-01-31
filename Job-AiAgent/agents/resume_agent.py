import os
import google.generativeai as genai
from dotenv import load_dotenv
from PyPDF2 import PdfReader

load_dotenv(os.path.join(os.path.dirname(__file__), '../../config/.env'))

def read_resume(file_path: str) -> str:
    """Extract text from PDF resume"""
    try:
        with open(file_path, "rb") as f:
            reader = PdfReader(f)
            return " ".join([page.extract_text() for page in reader.pages])
    except Exception as e:
        raise RuntimeError(f"Resume reading failed: {str(e)}")

def tailor_resume(job_desc: str, resume_text: str) -> str:
    """Use Gemini to optimize resume for specific job"""
    try:
        genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
        model = genai.GenerativeModel('gemini-pro')
        
        prompt = f"""Optimize this resume for the job description below. 
        Keep it ATS-friendly. Focus on matching keywords:
        
        JOB DESCRIPTION:
        {job_desc}
        
        ORIGINAL RESUME:
        {resume_text}
        
        Return ONLY the improved resume text:"""
        
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        raise RuntimeError(f"Resume tailoring failed: {str(e)}")