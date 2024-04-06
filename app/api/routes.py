from flask import jsonify, render_template
from flask_jwt_extended import get_jwt_identity, jwt_required

from app.api import bp
from app.extensions import db
from app.helper.role_based_authentication import role_required
from app.models.post import Post


@bp.route('/posts', methods=['GET'])
def get_posts():
    posts = []
    query_result = Post.query.all()

    for post in query_result:
        posts.append({'title': post.title, 'content': post.content})
    return jsonify({'posts': posts})

@bp.route('/protected', methods=['GET', 'POST'])
@jwt_required()
def protected():
    current_user = get_jwt_identity()
    print(current_user)
    return jsonify({'hello': 'world'}), 200

@bp.route('/only_admin', methods=['GET', 'POST'])
@jwt_required()
@role_required('admin')
def only_admin():
    current_user = get_jwt_identity()
    print(current_user)
    return jsonify({'msg': 'Welcome Admin'}), 200