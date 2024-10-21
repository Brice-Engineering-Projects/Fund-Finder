"""
__init__ file for Flask.   Contains the initialization code for the Flask app.

This file allows Python to treat the directory as a module and helps with
imports between different files within that package. The file can be empty or
can include initialization code.
"""

from flask import Flask
from config.config import DevelopmentConfig, ProductionConfig, TestingConfig


def create_app():
    """Initialization for Flask."""
    app = Flask(__name__)

    # Load configuration
    app.config.from_object(DevelopmentConfig)

    # Register routes from views
    from .views import main_blueprint
    app.register_blueprint(main_blueprint)

    return app
