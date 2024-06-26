from flask import render_template
from app.routes.posts import bp
from app.extensions import db
from app.models.post import Post

@bp.route('/')
def index():
    posts = Post.query.all()
    return render_template('archive/posts/index.html', posts=posts)