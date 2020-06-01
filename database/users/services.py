from app import db
from .model import User

class UserService(object):
    @staticmethod    
    def find_all():
        return User.query.all()

    @staticmethod
    def find_one(id: int):
        user = User.query.get(int(id)).first()
        if user:
            return user
        return { 'error': 'User does not exists!' }

    @staticmethod
    def create_one(email: str, password: str):
        try:
            user = User(email=email, password_hash=password)
            db.session.add(user)
            db.session.commit()
            return user
        except Exception as e:
             return { 'error': 'E-Mail already taken!' }

    @staticmethod
    def update_one(id: int, email: str):
        user = User.query.get(int(id))
        if user:
            user.email = email
            db.session.commit()
            return user
        return { 'error': 'User does not exists!' }

    @staticmethod
    def delete_one(id: int):
        user = User.query.get(int(id))
        if user:
            db.session.delete(user)
            db.session.commit()
            return user
        return { 'error': 'User does not exists!' }
