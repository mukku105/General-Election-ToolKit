from flask import Blueprint

bp = Blueprint('questions', __name__)

from app.routes.questions import routes