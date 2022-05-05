from dataclasses import dataclass
from datetime import datetime
from typing import List

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.dialects import postgresql
from elasticsearch import Elasticsearch

es = Elasticsearch('http://localhost:9200')
db = SQLAlchemy()

class Posts(db.Model):  # type: ignore
    id = db.Column(db.Integer, primary_key=True, index=True)
    rubrics = db.Column(postgresql.ARRAY(db.String), nullable=False)
    text = db.Column(db.UnicodeText, nullable=False)
    created_date = db.Column(db.DateTime, nullable=False)

@dataclass
class Post:
    id: int
    rubrics: List[str]
    text: str
    created_date: datetime
