from marshmallow import Schema, fields

class CarInputBodySchema(Schema):
    name = fields.String(required=True)
    brand = fields.String(required=True)
    model = fields.String(required=True)
    price = fields.String(required=True)
    image_url = fields.URL(required=True)

class CarUpdateBodySchema(Schema):
    name = fields.String()
    brand = fields.String()
    model = fields.String()
    price = fields.String()
    image_url = fields.URL()