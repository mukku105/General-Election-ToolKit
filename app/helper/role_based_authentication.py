from functools import wraps
from flask import jsonify
from flask_jwt_extended import get_jwt_identity
from app.models.user import Role

# Role Based Authentication Decorator
def role_required(role):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            current_user = get_jwt_identity()
            if current_user['role_id'] != Role.query.filter_by(name=role).first().id:
                return jsonify({'message': 'Access Denied! You are not authorized to access this resource'})
            else:
                return func(*args, **kwargs)
        return wrapper
    return decorator