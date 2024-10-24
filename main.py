"""App File for Grant API."""

# import logging
import sys
import os
from flask import render_template, request, redirect  # flash
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


@app.route("/basic-info", methods=['GET', 'POST'])
def basic_info():
    """Basic Information of the form, Section 1."""
    if request.method == 'POST':
        # Handle the form submission data here
        project_title = request.form.get('project-title')
        project_type = request.form.get('project-type')
        municipality = request.form.get('municipality')
        project_description = request.form.get('project_description')

        # For now, let's just print or process the data (you can store it or
        # use it for other logic)
        print(f"Title: {project_title}, Type: {project_type}, "
              f"Municipality: {municipality}, "
              f"Description: {project_description}")

        # Redirect or render the next page
        return redirect('/basic-info')

    # For GET request, just render the form
    return render_template("basic-info.html")


if __name__ == '__main__':
    app.run(debug=True)
