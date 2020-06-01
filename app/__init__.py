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
from database.items.services import ItemService
from database.orders.services import OrderService, CustomerService

user_service = UserService()
account_service = AccountService()
item_service = ItemService()
order_service = OrderService()
customer_service = CustomerService()

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

@app.route('/account', methods=['GET', 'POST'])
def account_route():
    body = request.json

    if request.method == 'POST':
        account = account_service.create_one(user_id=body['user_id'], allias=body['allias'], avatar=body['avatar'])

        if type(account) is dict and 'error' in account:
            return jsonify({ 'error': account.get('error') }), 500

        return jsonify({ 'account': account }), 201

    else:
        user_id = int(body['user_id'])
        print(user_id)
        accounts = account_service.find_all(user_id=user_id)
        return jsonify({ 'accounts': accounts }), 200