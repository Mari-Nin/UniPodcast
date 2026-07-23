
from src.ext import db
from src.models import BaseModel

class Category(BaseModel):
    __tablename__ = 'categories'

    category = db.Column(db.String(32))

    videos = db.relationship("Video",back_populates="category")
    news = db.relationship("News",back_populates="category")

    
    def __repr__(self):
        return self.category