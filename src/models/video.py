
from src.ext import db
from src.models import BaseModel

tag_video = db.Table('tag_video',
    db.Column('video_id',db.Integer,db.ForeignKey('videos.id'),primary_key=True),
    db.Column('tag_id',db.Integer,db.ForeignKey('tags.id'),primary_key=True)
)

class Video(BaseModel):
    __tablename__ = 'videos'
    title = db.Column(db.String(),nullable = False)
    img = db.Column(db.String(64), nullable=False)
    description = db.Column(db.Text, nullable=False)
    guests = db.Column(db.String(128), nullable=False)
    duration = db.Column(db.String, nullable=False)
    video_link = db.Column(db.String,nullable = False)
    in_slider = db.Column(db.Boolean, default=False)
    uploaded_at = db.Column(db.Date, nullable=False)

    category_id = db.Column(db.Integer,db.ForeignKey("categories.id"),nullable=False)
    category = db.relationship('Category',back_populates = 'videos')

    tag = db.relationship('Tag',secondary = tag_video,back_populates='videos')

    type_id = db.Column(db.Integer,db.ForeignKey('types.id'),nullable=False)
    type = db.relationship('Type',back_populates='videos')

    def __repr__(self):
        return self.title

























