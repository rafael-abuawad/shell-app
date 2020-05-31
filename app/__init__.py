from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from .config import Config

app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)
migrate = Migrate(app, db)

from database import User, Account, Item, Order, Customer

@app.route('/')
def index():
    print(User.query.all())
    return 'Hello World from Flask!'