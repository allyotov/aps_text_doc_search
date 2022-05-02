from dataclasses import dataclass

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Posts(db.Model):  # type: ignore
    uid = db.Column(db.Integer, primary_key=True)
    id = db.Column(db.Integer, nullable=False)
    rubrics = db.Column(db.String, nullable=False)
    text = db.Column(db.String, nullable=False)
    date_created = db.Column(db.String, nullable=False)


@dataclass
class Post:
    id: int
    rubrics: str
    text: str
    date_created: str
