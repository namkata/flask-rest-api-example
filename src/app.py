from flask import Flask

from config import Config
from routes import bp as routes_bp
from db import initialize_extensions


def create_app(config_class=Config):
    """
    Creates and configures the Flask application.

    Returns:
        Flask: The Flask application instance.
    """
    # Create Flask app instance
    app = Flask(__name__)

    # Load configurations from Config class
    app.config.from_object(config_class)

    # Initialize extensions with the app
    initialize_extensions(app)

    # Register blueprints or routes
    register_blueprints(app)

    return app



def register_blueprints(app):
    # Import and register blueprints or routes
    app.register_blueprint(routes_bp, url_prefix='/api')  # Register the blueprint with a URL prefix

# Create the app instance
app = create_app()

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000)
