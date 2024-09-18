from flask import Flask, send_from_directory
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os

# Initialize SQLAlchemy
db = SQLAlchemy()

def create_app():
    # Create the Flask application instance
    app = Flask(__name__, static_folder='static/build', template_folder='static/build')
    
    # Load configuration from the config module
    app.config.from_object('config.Config')

    # Initialize extensions
    db.init_app(app)
    migrate = Migrate(app, db)

    # Route to serve the React app
    @app.route('/')
    def index():
        return send_from_directory(app.static_folder, 'index.html')

    @app.route('/<path:path>')
    def serve_static(path):
        return send_from_directory(app.static_folder, path)

    with app.app_context():
        # Import routes after the app context is set up
        from . import routes
        db.create_all()

    return app
