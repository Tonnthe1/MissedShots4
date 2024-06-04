from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail
from config import Config

db = SQLAlchemy()
mail = Mail()

def create_app():
    app = Flask(__name__, template_folder='../templates', static_folder='../static')
    app.config.from_object(Config)
    
    db.init_app(app)
    mail.init_app(app)
    
    with app.app_context():
        # Import routes here to avoid circular imports
        from . import routes, models
        db.create_all()
    
    return app
