
from src.ext import db
from src.models import BaseModel

class Video(BaseModel):
    __tablename__ = 'video'
    title = db.Column(db.String(),nullable = False)
    img = db.Column(db.String(64), nullable=False)
    description = db.Column(db.Text, nullable=False)
    guests = db.Column(db.String(128), nullable=False)
    duration = db.Column(db.Time, nullable=False)
    uploaded_at = db.Column(db.Date, nullable=False)
    video_link = db.Column(db.String,nullable = True)
    in_slider = db.Column(db.Boolean, default=False)

    category_id = db.Column(db.Integer,db.ForeignKey("category.id"))
    
    category = db.relationship('Category',back_populates = 'videos')

    

























