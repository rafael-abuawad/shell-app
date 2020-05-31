from app import db

class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    title = db.Column(db.String(64))
    description = db.Column(db.String(256))
    picture = db.Column(db.String(64))
