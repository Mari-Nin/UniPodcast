from src.ext import db
from src.models.base import BaseModel


class Message(BaseModel):
    __tablename__ = 'messages'

    name = db.Column(db.String(16),nullable = False)
    surname = db.Column(db.String(16),nullable = False)
    text = db.Column(db.Text(),nullable=False)
    phone_number = db.Column(db.String(12))
    company = db.Column(db.String(16))
    company_text = db.Column(db.Text())


