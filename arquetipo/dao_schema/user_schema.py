from flask_marshmallow import Marshmallow
from marshmallow import Schema, fields
ma = Marshmallow()


class UserSchema(ma.Schema):
       id = fields.Integer()
       username = fields.String()
       email = fields.String()
       password = fields.String()

