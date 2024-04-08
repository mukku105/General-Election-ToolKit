from flask import render_template, request, url_for, redirect
from app.routes.accounts import bp
from app.extensions import db
from app.models.user import User
from flask_security import LoginForm

@bp.route('/', methods=['GET', 'POST'])
def index():
    users = User.query.all()
    # return "This is user index " + str(users)
    return render_template('accounts/index.html', users=users)