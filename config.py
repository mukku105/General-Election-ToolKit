import os, random, string
from datetime import timedelta
from flask_security import uia_phone_mapper
BASE_DIR = os.path.dirname(os.path.realpath(__file__))

class Config:
    # SQLALCHEMY_DATABASE_URI = 'mysql://root:Mukku%40105@localhost:3306/test_flask'
    # SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASE_DIR, 'app.db')

    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(hours=1)

    SECRET_KEY = os.getenv('SECRET_KEY', "a4b7d02885f4163d6913e9dbd24f2b20251d0b111fb68f89e835e87bef4f35e8")
    # SECURITY_USER_IDENTITY_ATTRIBUTES = [{"username": {"case_insensitive": True}}]
    SECURITY_PASSWORD_SALT = os.getenv('SECURITY_PASSWORD_SALT', "a4b7d02885f41ert6913e9dbd24f2b20251d0b111fb68f89e835errkkguyy5e8")

    JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY', "43af0b06301ad61d6584eec0c61a67979b7baf38dd28bb020ee234c5e05aab20")

    DB_ENGINE   = os.getenv('DB_ENGINE'   , None)
    DB_USERNAME = os.getenv('DB_USERNAME' , None)
    DB_PASS     = os.getenv('DB_PASS'     , None)
    DB_HOST     = os.getenv('DB_HOST'     , None)
    DB_PORT     = os.getenv('DB_PORT'     , None)
    DB_NAME     = os.getenv('DB_NAME'     , None)

    USE_SQLITE  = True 

    if DB_ENGINE and DB_NAME and DB_USERNAME:
        try:
            SQLALCHEMY_DATABASE_URI = '{}://{}:{}@{}:{}/{}'.format(
                DB_ENGINE,
                DB_USERNAME,
                DB_PASS,
                DB_HOST,
                DB_PORT,
                DB_NAME
            )
            USE_SQLITE  = False
        except Exception as e:
            print('> Error: DBMS Exception: ' + str(e) )
            print('> Fallback to SQLite ')

    if USE_SQLITE:
        DB_FOLDER = os.path.join(BASE_DIR, 'db')
        if not os.path.exists(DB_FOLDER):
            os.makedirs(DB_FOLDER)
        SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(DB_FOLDER, 'db.sqlite3')