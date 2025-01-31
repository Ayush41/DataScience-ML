import streamlit as st
import os
import json
from agents.scraper_agent import scrape_jobs
from agents.resume_agent import read_resume, tailor_resume
from agents.email_agent import send_application
from workflows.crewai_setup import setup_crewai_workflow

# UI Configuration
st.set_page_config(page_title="AI Job Assistant", layout="wide")

def main():
    st.title("🤖 AI Job Application Assistant")
    
    with st.sidebar:
        st.header("Configuration")
        job_query = st.text_input("Job keywords", "Software Engineer")
        location = st.text_input("Location", "New York")
        resume_file = st.file_uploader("Upload Resume (PDF)", type="pdf")
    
    if st.button("Start Job Search"):
        if resume_file:
            # Save uploaded resume
            resume_path = os.path.join("data", "user_resume.pdf")
            with open(resume_path, "wb") as f:
                f.write(resume_file.getbuffer())
            
            # Run workflow
            process = setup_crewai_workflow()
            result = process.execute()
            
            st.success("Applications sent successfully!")
            st.json(result)
        else:
            st.error("Please upload a resume first")

if __name__ == "__main__":
    main()