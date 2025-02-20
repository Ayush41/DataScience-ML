# app.py
from flask import Flask, render_template, request, jsonify
import requests
from bs4 import BeautifulSoup
import re
from difflib import SequenceMatcher

app = Flask(__name__)

# Mock job data structure (replace with actual scraping in production)
class JobScraper:
    def __init__(self):
        self.mock_jobs = [
            {
                'title': 'Python Developer',
                'company': 'Tech Corp',
                'location': 'Remote',
                'description': 'Seeking Python developer with 3+ years experience in Flask and AI/ML',
                'salary': '$80,000 - $100,000',
                'experience': '3-5 years'
            },
            {
                'title': 'Frontend Developer',
                'company': 'Web Inc',
                'location': 'New York',
                'description': 'Looking for React/Vue expert with 2+ years experience',
                'salary': '$70,000 - $90,000',
                'experience': '2-4 years'
            }
        ]

    def scrape_jobs(self, filters):
        # In real implementation, this would scrape actual job sites
        filtered_jobs = self.mock_jobs
        if filters.get('title'):
            filtered_jobs = [job for job in filtered_jobs if filters['title'].lower() in job['title'].lower()]
        if filters.get('location'):
            filtered_jobs = [job for job in filtered_jobs if filters['location'].lower() in job['location'].lower()]
        if filters.get('min_experience'):
            filtered_jobs = [job for job in filtered_jobs if self.extract_years(job['experience'])[0] >= int(filters['min_experience'])]
        return filtered_jobs

    def extract_years(self, experience_str):
        numbers = re.findall(r'\d+', experience_str)
        return [int(n) for n in numbers]

class ResumeAnalyzer:
    def analyze_match(self, resume_text, job_description):
        # Simple similarity analysis using SequenceMatcher
        similarity = SequenceMatcher(None, resume_text.lower(), job_description.lower()).ratio()
        score = similarity * 100
        feedback = {
            'score': round(score, 2),
            'comment': self.generate_feedback(score)
        }
        return feedback

    def generate_feedback(self, score):
        if score > 80:
            return "Excellent match! Your resume aligns well with the job requirements."
        elif score > 60:
            return "Good match. Consider highlighting more relevant skills."
        else:
            return "Fair match. You might need to tailor your resume more closely to this position."

scraper = JobScraper()
analyzer = ResumeAnalyzer()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/search', methods=['POST'])
def search_jobs():
    filters = {
        'title': request.form.get('title', ''),
        'location': request.form.get('location', ''),
        'min_experience': request.form.get('experience', '')
    }
    jobs = scraper.scrape_jobs(filters)
    return jsonify({'jobs': jobs})

@app.route('/analyze', methods=['POST'])
def analyze_resume():
    resume_text = request.form.get('resume', '')
    job_description = request.form.get('job_description', '')
    analysis = analyzer.analyze_match(resume_text, job_description)
    return jsonify(analysis)

if __name__ == '__main__':
    app.run(debug=True)