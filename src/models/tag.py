
from src.models.base import BaseModel
from src.ext import db
from src.models.news import tag_news
from src.models.video import tag_video

class Tag(BaseModel):
    __tablename__ = 'tags'

    name = db.Column(db.String,nullable = False)

    news = db.relationship('News',secondary=tag_news,back_populates = 'tag')
    videos = db.relationship('Video',secondary=tag_video,back_populates = 'tag')

    def __repr__(self):
        return self.name