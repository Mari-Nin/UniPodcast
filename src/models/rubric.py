from src.ext import db
from src.models import BaseModel

class Rubric(BaseModel):
    __tablename__ = 'rubric'

    title = db.Column(db.String, nullable=False)
    img = db.Column(db.String(64), nullable=False)
    description = db.Column(db.Text, nullable=False)
    duration = db.Column(db.Time, nullable=False)
    uploaded_at = db.Column(db.Date, nullable=False)
    rubric_link = db.Column(db.String,nullable = True)

    category_id = db.Column(db.Integer, db.ForeignKey("category.id"))
    rubric_link = db.Column(db.String,nullable = True)
    
    category = db.relationship("Category",back_populates='rubrics')




