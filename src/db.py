from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# Initialize extensions
db = SQLAlchemy()
migrate = Migrate()

def initialize_extensions(app):
    # Initialize extensions with the app
    db.init_app(app)
    migrate.init_app(app, db)
    # Initialize other extensions here if needed