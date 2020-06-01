from app import db
from werkzeug.security import generate_password_hash, check_password_hash 

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(64), unique=True, nullable=False)
    password_hash = db.Column(db.String(96))
    active = db.Column(db.Boolean, default=True)
    accounts = db.relationship('Account', backref='user', lazy=True)
    items = db.relationship('Item', backref='user', lazy=True)
    orders = db.relationship('Order', backref='user', lazy=True)
    customers = db.relationship('Customer', backref='user', lazy=True)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return f'<User: {self.email}>'

class Account(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    avatar = db.Column(db.String(8))
    allias = db.Column(db.String(16))

    def __repr__(self):
        return f'<User: {self.allias}>'
