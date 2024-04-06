from flask import Blueprint

bp = Blueprint('accounts', __name__)

from app.routes.accounts import routes