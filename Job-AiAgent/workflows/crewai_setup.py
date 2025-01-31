from crewai import Agent, Task, Process
from ..agents import scraper_agent, resume_agent, email_agent

def setup_crewai_workflow():
    # Define Agents
    scraper = Agent(
        role='Job Scraper',
        goal='Find relevant job postings',
        backstory="Expert in scraping job boards for opportunities",
        tools=[scraper_agent.scrape_jobs],
        verbose=True
    )
    
    resume_writer = Agent(
        role='Resume Expert',
        goal='Optimize resumes for ATS systems',
        backstory="Professional resume writer with technical skills",
        tools=[resume_agent.tailor_resume],
        verbose=True
    )
    
    email_sender = Agent(
        role='Application Coordinator',
        goal='Send job applications',
        backstory="Efficient communicator handling applications",
        tools=[email_agent.send_application],
        verbose=True
    )
    
    # Define Tasks
    scrape_task = Task(
        description="Find software engineering jobs in New York",
        agent=scraper,
        expected_output="List of 5 job opportunities"
    )
    
    resume_task = Task(
        description="Optimize resume for first job listing",
        agent=resume_writer,
        context=[scrape_task],
        expected_output="ATS-optimized resume text"
    )
    
    email_task = Task(
        description="Send application for first job",
        agent=email_sender,
        context=[resume_task],
        expected_output="Confirmation of sent application"
    )
    
    return Process(
        agents=[scraper, resume_writer, email_sender],
        tasks=[scrape_task, resume_task, email_task],
        verbose=True
    )