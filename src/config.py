import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))


# Find the .env file in the root directory and load the variables
dotenv_path = os.path.join(basedir, ".env")
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'your_default_secret_key'
    DEBUG = os.environ.get('DEBUG') == 'True'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URI')
    SQLALCHEMY_TRACK_MODIFICATIONS = os.environ.get('SQLALCHEMY_TRACK_MODIFICATIONS', False)

    # Add more configurations as needed

    # For example, setting up other Flask configurations:
    # CSRF_ENABLED = True
    # SESSION_COOKIE_SECURE = True
    # ...

    # Ensure that the .env variables are loaded
    if not SECRET_KEY:
        raise ValueError("No SECRET_KEY set for Flask application.")
    if not SQLALCHEMY_DATABASE_URI:
        raise ValueError("No DATABASE_URI set for Flask application.")
