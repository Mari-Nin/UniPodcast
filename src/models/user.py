from flask_login import UserMixin
from werkzeug.security import generate_password_hash

from src.ext import db
from src.models import BaseModel


class User(BaseModel,UserMixin):
    __tablename__ ='users'

    username = db.Column(db.String,nullable=False)
    _password = db.Column(db.String,nullable=False)
    role = db.Column(db.String, default='admin')


    @property
    def password(self):
        return self._password
    
    @password.setter
    def password(self,password):
        self._password = generate_password_hash(password)
   
    def __repr__(self):
        return self.name