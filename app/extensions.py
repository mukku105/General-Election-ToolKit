from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from flask_security import Security, SQLAlchemyUserDatastore
from flask_migrate import Migrate

security = Security()
user_datastore = SQLAlchemyUserDatastore(None, None, None)
db = SQLAlchemy()
migrate = Migrate()
jwt = JWTManager()