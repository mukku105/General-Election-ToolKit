from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView

from flask_jwt_extended import JWTManager, jwt_required, create_access_token
from werkzeug.security import generate_password_hash, check_password_hash
from flask_security import SQLAlchemyUserDatastore

from app.models.user import User, Role
from config import Config
from app.extensions import db, jwt, security, user_datastore

from app.flask_admin import initialize_admin

def create_app(config_class=Config):
    app = Flask(__name__, static_folder='static')
    app.config.from_object(config_class)

    # Initialize Flask extensions here
    db.init_app(app)
    jwt.init_app(app)

    user_datastore = SQLAlchemyUserDatastore(db, User, Role)
    security.init_app(app, user_datastore)
    
    # Initialize Flask Admin
    initialize_admin.create_flask_admin(app, db)

    # Register blueprints
    from app.routes.main import bp as main_bp
    app.register_blueprint(main_bp)

    from app.routes.posts import bp as posts_bp
    app.register_blueprint(posts_bp, url_prefix='/posts')

    from app.routes.questions import bp as questions_bp
    app.register_blueprint(questions_bp, url_prefix='/questions')

    from app.routes.accounts import bp as accounts_bp
    app.register_blueprint(accounts_bp, url_prefix='/accounts')

    from app.routes.admins import bp as admin_bp
    app.register_blueprint(admin_bp, url_prefix='/admins')

    from app.api import bp as api_bp
    app.register_blueprint(api_bp, url_prefix='/api')

    @app.route('/test/')
    def test_page():
        return '<h1>Testing the Flask Application Factory Pattern</h1>'

    return app