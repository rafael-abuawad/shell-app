from app import db
from .models import User, Account

class UserService(object):
    @staticmethod    
    def find_all():
        users = User.query.all()
        return users

    @staticmethod
    def find_one(id: int):
        user = User.query.get(id)
        if user:
            return user
        return { 'error': 'User does not exists!' }

    @staticmethod
    def create_one(email: str, password: str):
        try:
            user = User(email=email)
            user.set_password(password)
            db.session.add(user)
            db.session.commit()
            return user
        except Exception as e:
             return { 'error': 'E-Mail already taken!' }

    @staticmethod
    def update_one(id: int, email: str):
        user = User.query.get(id)
        if user:
            user.email = email
            user.active = active
            db.session.commit()
            return user
        return { 'error': 'User does not exists!' }

    @staticmethod
    def delete_one(id: int):
        user = User.query.get(id)
        if user:
            db.session.delete(user)
            db.session.commit()
            return user
        return { 'error': 'User does not exists!' }

    @staticmethod
    def update_activate_user(id: int, active: bool):
        user = User.query.get(id)
        if user:
            user.active = active
            db.session.commit()
            return user
        return { 'error': 'User does not exists!' }

class AccountService(object):
    @staticmethod    
    def find_all(user_id: int):
        user = User.query.get(user_id)
        return user.accounts

    @staticmethod
    def find_one(id: int):
        account = Account.query.get(id)
        if account:
            return account
        return { 'error': 'Account does not exists!' }

    @staticmethod
    def create_one(user_id: int, allias: str, avatar: str):
        user = User.query.get(user_id)
        
        if not user:
            return { 'error': 'User does not exists!' }

        if len(user.accounts) >= 3:
            return { 'error': 'User\'s accounts quota reached!' }

        account = Account(user=user, avatar=avatar, allias=allias)
        db.session.add(account)
        db.session.commit()
        return account

    @staticmethod
    def update_one(id: int, avatar: str, allias: str):
        account = Account.query.get(int(id))
        if account:
            account.avatar = avatar
            account.allias = allias
            db.session.commit()
            return account
        return { 'error': 'Account does not exists!' }

    @staticmethod
    def delete_one(id: int):
        account = Account.query.get(id)
        if account:
            db.session.delete(account)
            db.session.commit()
            return account
        return { 'error': 'Account does not exists!' }
