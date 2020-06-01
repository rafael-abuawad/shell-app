from app import ma

class UserSchema(ma.Schema):
    class Meta:
        fields = ("email", "active")

user_schema = UserSchema()
users_schema = UserSchema(many=True)

class AccountSchema(ma.Schema):
    class Meta:
        fields = ("avatar", "allias")

account_schema = AccountSchema()
accounts_schema = AccountSchema(many=True)
