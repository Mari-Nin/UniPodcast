
from src.ext import db
from src.models import BaseModel

class Category(BaseModel):
    __tablename__ = 'category'

    category = db.Column(db.String(16))

    videos = db.relationship("Video",back_populates="category")
    rubrics = db.relationship("Rubric",back_populates="category")


    def __str__(self):
        return self.category