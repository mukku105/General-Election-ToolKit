from flask import Blueprint

bp = Blueprint('toolkit', __name__)

from app.routes.toolkit import routes_ps
from app.routes.toolkit import routes_ac_el_officer