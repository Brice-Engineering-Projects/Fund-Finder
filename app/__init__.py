"""
app/__init__.py

__init__ file for Flask.   Contains the initialization code for the Flask app.

This file allows Python to treat the directory as a module and helps with
imports between different files within that package. The file can be empty or
can include initialization code.
"""

import os
from flask import Flask
from flask_debugtoolbar import DebugToolbarExtension
from app.config.settings import DevelopmentConfig, ProductionConfig, TestingConfig


def create_app(env='development'):
    """
    Factory function that creates and configures the Flask application
    based on the environment (development, production, or testing).
    """
    app = Flask(__name__, template_folder="templates")

    # Dynamically load the configuration based on the environment
    if env == 'development':
        app.config.from_object(DevelopmentConfig)
    elif env == 'production':
        app.config.from_object(ProductionConfig)
    elif env == 'testing':
        app.config.from_object(TestingConfig)
    else:
        raise ValueError(f"Invalid environment: {env}")

    # Load the SECRET_KEY and other variables from environment
    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'supersecret')

    # Register routes from views using relative import
    from app.api.routes import main_blueprint
    app.register_blueprint(main_blueprint)

    # Enable Debug Toolbar in development
    if app.config.get('DEBUG', False):
        DebugToolbarExtension(app)

    return app
