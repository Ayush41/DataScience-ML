import os
import json
from langchain_community.tools import SerpAPIWrapper
from dotenv import load_dotenv

load_dotenv(os.path.join(os.path.dirname(__file__), '../../config/.env'))

def scrape_jobs(query: str, location: str = "") -> list:
    """Scrape job listings using SerpAPI"""
    try:
        search = SerpAPIWrapper()
        results = search.run(f"{query} jobs {location}".strip())
        
        # Simple parsing (customize based on your needs)
        jobs = []
        if isinstance(results, list):
            for job in results:
                jobs.append({
                    "title": job.get("title", ""),
                    "company": job.get("company", ""),
                    "location": job.get("location", ""),
                    "description": job.get("description", ""),
                    "apply_link": job.get("link", "")
                })
        return jobs[:5]  # Return first 5 results
        
    except Exception as e:
        print(f"Scraping error: {str(e)}")
        return []