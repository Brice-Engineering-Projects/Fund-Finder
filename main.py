"""App File for Grant API."""

# import logging
import sys
import os
from flask import render_template  # request, redirect, flash
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


if __name__ == '__main__':
    app.run(debug=True)
