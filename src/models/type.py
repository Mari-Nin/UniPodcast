
from src.ext import db
from src.models.base import BaseModel


class Type(BaseModel):
    __tablename__ = 'types'
    name = db.Column(db.String,nullable = False)

    news = db.relationship('News',back_populates = 'type')
    videos = db.relationship('Video',back_populates = 'type')

    def __repr__(self):
        return self.name