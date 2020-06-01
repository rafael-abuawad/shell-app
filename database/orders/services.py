from app import db
from .models import Order, Customer
from database.users.models import User

class OrderService(object):
    @staticmethod    
    def find_all(user_id: int):
        user = User.query.get(user_id)
        return user.orders

    @staticmethod
    def find_one(id: int):
        order = Order.query.get(id)
        if order:
            return order
        return { 'error': 'Order does not exists!' }

    @staticmethod
    def create_one(user_id: int, total: float, address: str, date_created, date_delivery, customer_id: int, items_id):

        user = User.query.get(user_id)
        if not user:
            return { 'error': 'User does not exists!' }
       
        customer = Customer.query.get(customer_id)
        if not customer:
            return { 'error': 'Customer does not exists!' }

        order = Order(user=user, total=total, address=address, date_created=date_created, date_delivery=date_delivery, customer=customer)

        for item_id in items_id:
            item = Item.query.get(item_id)
            if not item:
                return { 'error': 'Item does not exists!' }
            else:
                order.add_order_items(item)

        db.session.add(order)
        db.session.commit()
        return order

    @staticmethod
    def delete_one(id: int):
        order = Order.query.get(int(id))
        if order:
            db.session.delete(order)
            db.session.commit()
            return order
        return { 'error': 'Order does not exists!' }

class CustomerService(object):
    @staticmethod    
    def find_all(user_id: int):
        user = User.query.get(user_id)
        return user.customers

    @staticmethod
    def find_one(id: int):
        customer = Customer.query.get(id)
        if customer:
            return order
        return { 'error': 'Customer does not exists!' }

    @staticmethod
    def create_one(user_id: int, first_name: str, last_name: str, cellphone_number: str):
        user = User.query.get(user_id)

        if not user:
            return { 'error': 'User does not exists!' }

        customer = Customer(user=user, first_name=first_name, last_name=last_name, cellphone_number=cellphone_number)
        db.session.add(customer)
        db.session.commit()
        return customer

    @staticmethod
    def update_one(id: int, first_name: str, last_name: str, cellphone_number: str):
        customer = Customer.query.get(id)
        if not customer:
            return { 'error': 'Customer does not exists!' }

        customer.first_name = first_name
        customer.last_name = last_name
        customer.cellphone_number = cellphone_number
        db.session.commit()
        return customer

    @staticmethod
    def delete_one(id: int):
        customer = Customer.query.get(id)
        if customer:
            db.session.delete(customer)
            db.session.commit()
            return customer
        return { 'error': 'Customer does not exists!' }
