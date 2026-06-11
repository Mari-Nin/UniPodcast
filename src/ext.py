from flask_sqlalchemy import SQLAlchemy
from flask_admin import Admin
from flask_login import LoginManager
from flask_restx import Api


db = SQLAlchemy()
admin = Admin()
login_manager = LoginManager()
api=Api()
