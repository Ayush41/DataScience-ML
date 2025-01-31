import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from dotenv import load_dotenv

load_dotenv(os.path.join(os.path.dirname(__file__), '../../config/.env'))

def send_application(email_to: str, subject: str, body: str, resume_text: str):
    """Send job application email with resume"""
    try:
        msg = MIMEMultipart()
        msg['From'] = os.getenv("EMAIL_ADDRESS")
        msg['To'] = email_to
        msg['Subject'] = subject
        
        msg.attach(MIMEText(body, 'plain'))
        msg.attach(MIMEText(f"\n\nResume:\n{resume_text}", 'plain'))
        
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
            server.login(os.getenv("EMAIL_ADDRESS"), os.getenv("EMAIL_PASSWORD"))
            server.send_message(msg)
        return True
    except Exception as e:
        print(f"Email error: {str(e)}")
        return False