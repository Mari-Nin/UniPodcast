
from flask import Flask
from src.config import Config
from src.ext import db,admin,login_manager, api


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    register_extensions(app)

    return app
   
def  register_extensions(app):
    db.init_app(app)
    admin.init_app(app)
    login_manager.init_app(app)
    api.init_app(app)


