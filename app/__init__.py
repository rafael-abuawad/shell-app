from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_marshmallow import Marshmallow
from .config import Config

app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)
migrate = Migrate(app, db)
ma = Marshmallow(app)

from database import User, Account, Item, Order, Customer
from database.users.services import UserService, AccountService

user_service = UserService()

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        body = request.json
        user = user_service.create_one(email=body['email'], password=body['password'])

        if type(user) is dict and 'error' in user:
            return jsonify({ 'error': user.get('error') }), 500
        return jsonify({ 'user': user }), 201

    else:
        users = user_service.find_all()
        return jsonify({ 'users': users }), 200