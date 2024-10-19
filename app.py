"""App File for Grant API."""

# import logging
# import os

# # from flask import Flask, render_template, request, redirect, flash
# # from flask_sqlalchemy import SQLAlchemy
# # from flask_debugtoolbar import DebugToolbarExtension
# from dotenv import load_dotenv
# # from sqlalchemy.exc import SQLAlchemyError, IntegrityError

# from config import DevelopmentConfig, ProductionConfig, TestingConfig


# Load environment variables from .env file
# load_dotenv()

# Initialize the Flask application
# app = Flask(__name__)

# Load the SECRET_KEY and other configuration variables from .env file
# app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')

# Choose the configuration class based on FLASK_ENV from the .env file
# env = os.getenv('FLASK_ENV')

# if env == 'development':
#     app.config.from_object(DevelopmentConfig)
# elif env == 'production':
#     app.config.from_object(ProductionConfig)
# elif env == 'testing':
#     app.config.from_object(TestingConfig)
# else:
#     # Default to development if FLASK_ENV is missing
#     app.config.from_object(DevelopmentConfig)

# # Check if SECRET_KEY is loaded (debugging purpose)
# if not app.config.get('SECRET_KEY'):
#     raise RuntimeError("SECRET_KEY not found in Flask app config!")

# Enable Debug Toolbar for development
# debug = DebugToolbarExtension(app)


# if __name__ == '__main__':
#     app.run()
