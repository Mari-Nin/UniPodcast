from flask_login import UserMixin
from werkzeug.security import generate_password_hash

from src.ext import db
from src.models import BaseModel


class User(BaseModel,UserMixin):
    __tablename__ ='users'

    username = db.Column(db.String,nullable=False)
    _password = db.Column(db.String,nullable=False)
    role = db.Column(db.String, default='admin')
    #თუ მომავალში საჭირო გახდება ახალი უზერების შემოტანა

    @property
    def password(self):
        return self._password
    
    @password.setter
    def password(self,password):
        self._password = generate_password_hash(password)
   
    # def check_password(self, password):
    #     return check_password_hash(self._password, password)