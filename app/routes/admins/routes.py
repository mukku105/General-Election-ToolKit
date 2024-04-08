from flask import render_template
from flask_login import login_required

from app.routes.admins import bp
from app.extensions import db
from app.models.post import Post

@bp.route('/')
def index():
    posts = Post.query.all()
    return render_template('admins/index.html')