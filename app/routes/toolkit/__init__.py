from flask import Blueprint

bp = Blueprint('toolkit', __name__)

from app.routes.toolkit import routes