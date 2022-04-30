from marshmallow import Schema, fields, post_load

from searchapp.resources.models import Post


class PostSchema(Schema):
    id = fields.Int(required=True)
    rubrics = fields.Str(required=True)
    text = fields.Str(required=True)
    created_date = fields.DateTime(required=True)