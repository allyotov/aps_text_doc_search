from dataclasses import dataclass
from datetime import datetime

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Posts(db.Model):  # type: ignore
    id = db.Column(db.Integer, primary_key=True)
    rubrics = db.Column(db.String, nullable=False)
    text = db.Column(db.String, nullable=False)
    created_date = db.Column(db.DateTime, nullable=False)


@dataclass
class Post:
    rubrics: str
    text: str
    created_date: datetime
