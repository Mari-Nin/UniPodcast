from src.ext import db
from src.models.base import BaseModel


class Message(BaseModel):
    __tablename__ = 'messages'

    name = db.Column(db.String(32),nullable = False)
    surname = db.Column(db.String(32),nullable = False)
    text = db.Column(db.Text(),nullable=False)
    phone_number = db.Column(db.String(32),nullable=True)
    email = db.Column(db.String(128),nullable=False)
    company = db.Column(db.String(68),nullable=True)
    company_text = db.Column(db.Text(),nullable=True)
    seen = db.Column(db.Boolean, default = False)


