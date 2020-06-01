from app import db
from .models import Item
from database.users.models import User

class ItemService(object):
    @staticmethod    
    def find_all():
        items = Item.query.all()
        return items

    @staticmethod
    def find_one(id: int):
        item = Item.query.get(id)
        if item:
            return item
        return { 'error': 'Item does not exists!' }

    @staticmethod
    def create_one(user_id: int, title: str, description: str, picture: str):
        user = User.query.get(user_id)
        if not user:
            return { 'error': 'User does not exists!' } 
         
        item = Item(user=user, title=title, description=description, picture=picture)           
        db.session.add(item)
        db.session.commit()
        return item

    @staticmethod
    def update_one(id: int, title: str, description: str, picture: str):
        item = Item.query.get(id)
        if user:
            item.title = title
            item.description = description
            item.picture = picture
            user.active = active
            db.session.commit()
            return item
        return { 'error': 'Item does not exists!' }

    @staticmethod
    def delete_one(id: int):
        item = Item.query.get(id)
        if item:
            db.session.delete(item)
            db.session.commit()
            return item
        return { 'error': 'Item does not exists!' }

