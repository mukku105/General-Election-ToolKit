from flask import Blueprint

bp = Blueprint('admins', __name__)

from app.routes.admins import routes