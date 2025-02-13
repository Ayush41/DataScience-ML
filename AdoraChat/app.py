from flask import Flask, render_template, redirect, url_for, session
from flask_firebase import FirebaseAuth
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv('FLASK_SECRET_KEY')

# Firebase configuration
app.config['FIREBASE_API_KEY'] = os.getenv('FIREBASE_API_KEY')
app.config['FIREBASE_AUTH_DOMAIN'] = os.getenv('FIREBASE_AUTH_DOMAIN')
app.config['FIREBASE_PROJECT_ID'] = os.getenv('FIREBASE_PROJECT_ID')
app.config['FIREBASE_AUTH_SIGN_IN_OPTIONS'] = os.getenv('FIREBASE_AUTH_SIGN_IN_OPTIONS')
# Initialize FirebaseAuth
auth = FirebaseAuth(app)

# Routes    
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/pricing')
def pricing():
    return render_template('pricing.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect(url_for('home'))

@app.route('/dashboard')
def dashboard():
    if 'user' not in session:
        return redirect(url_for('login'))
    return render_template('dashboard.html')

@app.route('/profile')
def profile():
    if 'user' not in session:
        return redirect(url_for('login'))
    return "Profile Page (Placeholder)"

@app.route('/chat')
def chat():
    if 'user' not in session:
        return redirect(url_for('login'))
    return "Chat Page (Placeholder)"

if __name__ == '__main__':
    app.run(debug=True)