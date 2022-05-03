from marshmallow import Schema, fields


class PostSchema(Schema):
    id = fields.Int(required=True)
    rubrics = fields.Str(required=True)
    text = fields.Str(required=True)
    created_date = fields.DateTime(required=True)