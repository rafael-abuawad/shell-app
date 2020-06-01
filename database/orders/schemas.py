from app import ma

class OrderSchema(ma.Schema):
    class Meta:
        fields = ('user', 'customer', 'total', 'address',
                'date_created', 'date_delivery', 'items')

order_schema = OrderSchema()
orders_schema = OrderSchema(many=True)

class CustomerSchema(ma.Schema):
    class Meta:
        fields = ('first_name', 'last_name', 'cellphone_number')

customer_schema = OrderSchema()
customers_schema = OrderSchema(many=True)
