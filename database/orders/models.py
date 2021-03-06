from app import db
from datetime import datetime

order_items = db.Table('order_items',
    db.Column('order_id', db.Integer, db.ForeignKey('order.id'), primary_key=True),
    db.Column('item_id', db.Integer, db.ForeignKey('item.id'), primary_key=True),
)

order_customers = db.Table('order_customers',
    db.Column('order_id', db.Integer, db.ForeignKey('order.id'), primary_key=True),
    db.Column('customer_id', db.Integer, db.ForeignKey('customer.id'), primary_key=True),
)

class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    total = db.Column(db.Integer, default=0)
    address = db.Column(db.String(128), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)
    date_delivery = db.Column(db.DateTime)
    customer = db.relationship('Customer', secondary=order_customers, lazy='subquery',
                            backref=db.backref('orders', lazy=True))
    items = db.relationship('Item', secondary=order_items, lazy='subquery',
                            backref=db.backref('orders', lazy=True))

    def set_delivery_date(self, date):
        self.date_delivery = date

    def add_order_items(self, item):
        self.items.append(item)

    def __repr__(self):
        return f'<Order: {self.id}>'

class Customer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    first_name = db.Column(db.String(64))
    last_name = db.Column(db.String(64))
    cellphone_number = db.Column(db.String(16))

    def full_name(self):
        return f'{self.first_name} {self.last_name}'

    def __repr__(self):
        return f'<Customer: {self.first_name} {self.last_name}>'
