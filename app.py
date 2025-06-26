from flask import Flask, session, request
from flask_login import LoginManager, UserMixin
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_bcrypt import Bcrypt

db = SQLAlchemy()
login_manager = LoginManager()
migrate = Migrate()
bcrypt = Bcrypt()

@login_manager.user_loader
def load_user(user_id):
    from models import User
    if user_id == 'Jayden':
        return User('Jayden')
    return None

def create_app():
    app = Flask(__name__, template_folder = 'templates', static_folder= 'static', static_url_path= '/')
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///./blueprints.db'
    app.secret_key = 'Some Key'
    
    
    db.init_app(app)
    login_manager.init_app(app)
    # login_manager_view = "auth.login"
    migrate.init_app(app, db)

    from blueprints.auth import auth_bp
    from blueprints.main import main_bp
    from blueprints.register import register_bp

    app.register_blueprint(auth_bp)
    app.register_blueprint(main_bp)
    app.register_blueprint(register_bp)

    return app

