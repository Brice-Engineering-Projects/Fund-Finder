"""
app/config/settings.py
Centralized configuration for Flask app.
"""

import os
import logging
from dotenv import load_dotenv, find_dotenv

# Load environment variables from a .env file
load_dotenv(find_dotenv())


class Config:
    """Base configuration."""
    SECRET_KEY = os.getenv('SECRET_KEY', 'default_secret_key')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'sqlite:///instance/default.db')

    # Session management
    SESSION_TYPE = 'Redis'
    SESSION_PERMANENT = False
    SESSION_USE_SIGNER = True

    # CSRF protection (for Flask-WTF)
    WTF_CSRF_ENABLED = True

    # Email config (optional, used for password reset or contact forms)
    MAIL_SERVER = os.getenv("MAIL_SERVER", "smtp.gmail.com")
    MAIL_PORT = int(os.getenv("MAIL_PORT", 587))
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.getenv("MAIL_USERNAME", None)
    MAIL_PASSWORD = os.getenv("MAIL_PASSWORD", None)
    MAIL_DEFAULT_SENDER = os.getenv("MAIL_DEFAULT_SENDER", MAIL_USERNAME)

    # Security best practices for production
    SESSION_COOKIE_HTTPONLY = True
    REMEMBER_COOKIE_HTTPONLY = True
    SESSION_COOKIE_SECURE = os.getenv("SESSION_COOKIE_SECURE", "False").lower() in ("true", "1", "t")

    # External APIs (e.g., Grants.gov)
    GRANTS_API_KEY = os.getenv("GRANTS_API_KEY", None)


class DevelopmentConfig(Config):
    """Development configuration."""
    DEBUG = True
    SQLALCHEMY_ECHO = True
    FLASK_ENV = 'development'
    USE_RELOADER = True
    DEBUG_TB_INTERCEPT_REDIRECTS = True


class ProductionConfig(Config):
    """Production configuration."""
    DEBUG = False
    SQLALCHEMY_ECHO = False
    FLASK_ENV = 'production'


class TestingConfig(Config):
    """Testing configuration."""
    TESTING = True
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = os.getenv('TEST_DATABASE_URL', 'sqlite:///instance/test.db')
    WTF_CSRF_ENABLED = False
    FLASK_ENV = 'testing'
    DEBUG_TB_HOSTS = 'dont-show-debug-toolbar'


# Initialize app-level logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG if os.getenv('FLASK_ENV') != 'production' else logging.INFO)

console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
console_handler.setFormatter(formatter)

logger.addHandler(console_handler)

