from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from flask_security import Security, SQLAlchemyUserDatastore

security = Security()
user_datastore = SQLAlchemyUserDatastore(None, None, None)
db = SQLAlchemy()
jwt = JWTManager()