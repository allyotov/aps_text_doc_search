from dataclasses import dataclass
from datetime import datetime

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func
from sqlalchemy import text, cast
from sqlalchemy.dialects import postgresql

db = SQLAlchemy()


def create_tsvector(*args):
    exp = args[0]
    for e in args[1:]:
        exp += ' ' + str(e)
    return func.to_tsvector('english', exp)

class Posts(db.Model):  # type: ignore
    id = db.Column(db.Integer, primary_key=True, index=True)
    rubrics = db.Column(db.String, nullable=False)
    text = db.Column(db.UnicodeText, nullable=False)
    created_date = db.Column(db.DateTime, nullable=False)


    __ts_vector__ = create_tsvector(
        cast(func.coalesce(text, ''), postgresql.TEXT)
    )

    __table_args__ = (
        db.Index(
            'idx_text_fts',
            __ts_vector__,
            postgresql_using='gin'
        ),
    )

@dataclass
class Post:
    id: int
    rubrics: str
    text: str
    created_date: datetime
