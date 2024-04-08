import datetime
import uuid
from app.extensions import db

from flask_security import UserMixin, RoleMixin, hash_password


roles_users = db.Table('roles_users',
    db.Column('user_id', db.Integer(), db.ForeignKey('user.id')),
    db.Column('role_id', db.Integer(), db.ForeignKey('role.id'))
)

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), unique=True, nullable=False)
    phone_no = db.Column(db.String(12), unique=True, nullable=False)
    full_name = db.Column(db.String(255), nullable=False)
    fs_uniquifier = db.Column(db.String(255), nullable=False)
    confirmed_at = db.Column(db.DateTime())
    password = db.Column(db.String(120), nullable=False)
    active = db.Column(db.Boolean())

    roles = db.relationship('Role', secondary=roles_users, backref=db.backref('users', lazy='dynamic'))

    def __repr__(self):
        return '<User %r>' % self.username
    
    def set_password(self, password):
        self.password = hash_password(password)
        
    def set_uuid(self):
        self.fs_uniquifier = str(uuid.uuid4())
    
    def __str__(self):
        return self.username

class Role(db.Model, RoleMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    description = db.Column(db.String(255))

    def __repr__(self):
        return '<Role %r>' % self.name
    
    def __str__(self):
        return self.name