from marshmallow import Schema, fields

class UserInputBodySchema(Schema):
    username = fields.String(required=True)
    email = fields.Email(required=True)
    password = fields.String(required=True)
    role = fields.String(missing='customer')