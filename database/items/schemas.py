from app import ma

class ItemSchema(ma.Schema):
    class Meta:
        fields = ('id', 'title', 'description', 'price', 'picture')

item_schema = ItemSchema()
items_schema = ItemSchema(many=True)
