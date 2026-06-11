
from src.ext import db
from src.models.base import BaseModel

class User(BaseModel):
    __tablename__ ='users'

    
    username = db.Column(db.String,nullable=False)
    password = db.Column(db.String,nullable=False)
    
    role = db.Column(db.String, default='user')
    # თუ მომავალში სგახდება საჭირო როლების დამატება