"""App File for Grant API."""

# import logging
import sys
import os
from flask import render_template, request, redirect, session  # flash
# from flask_sqlalchemy import SQLAlchemy
# from flask_debugtoolbar import DebugToolbarExtension
from dotenv import load_dotenv
# from sqlalchemy.exc import SQLAlchemyError, IntegrityError
from app import create_app  # Import the app factory function

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Load environment variables from .env file
load_dotenv()

# Determine the environment ('development', 'production', 'testing')
env = os.getenv('FLASK_ENV', 'development')

# Create the app based on the current environment
app = create_app(env)


@app.route("/")
def home():
    """Homepage."""
    return render_template("home.html")


# Route for Section 1: Basic Info
@app.route("/basic-info", methods=['GET', 'POST'])
def basic_info():
    """Basic Information of the form, Section 1."""
    if request.method == 'POST':
        # Capture the form data
        session['applicant_name'] = request.form['applicant-name']
        session['contact_person'] = request.form['contact-person']
        session['phone'] = request.form['phone']
        session['email'] = request.form['email']
        session['duns'] = request.form['duns']
        session['ein'] = request.form['ein']
        return redirect('project-details')
    return render_template("basic-info.html")


# Route for Section 2: Project Details
@app.route('/project-details', methods=['GET', 'POST'])
def project_details():
    """Project Details, Section 2."""
    if request.method == 'POST':
        # Capture the form data
        session['project_title'] = request.form['project-title']
        session['project_type'] = request.form['project-type']
        session['project_description'] = request.form['project-description']
        session['project_budget'] = request.form['project-budget']
        session['project_timeline'] = request.form['project-timeline']
        return redirect('funding-requirements')
    return render_template('project-details.html')


# Route for Section 3: Funding Requirements
@app.route('/funding-requirements', methods=['GET', 'POST'])
def funding_requirements():
    """Funding Requirements, Section 3."""
    if request.method == 'POST':
        # Capture the form data
        session['mhi'] = request.form['mhi']
        session['population'] = request.form['population']
        session['poverty_rate'] = request.form['poverty-rate']
        return redirect('review-submission')
    return render_template('funding-requirements.html')


# Route for Section 4: Review Submission
@app.route('/review-submission', methods=['GET', 'POST'])
def review_submission():
    """Review Submission, Section 4."""
    if request.method == 'POST':
        # Capture the final submission (you could send this data to a database
        # or API)
        return redirect('success')
    return render_template('review-submission.html', data=session)


# Success page after form submission
@app.route('/success')
def success():
    """Successful Submission Page."""
    return "Application submitted successfully!"


if __name__ == '__main__':
    app.run(debug=True)
