from flask import Flask

from src.admin_views import SecureIndexView
from src.admin_views import AdminUserView, CategoryView, RubricView, VideoView,MemberView,MessageView
from src.config import Config
from src.ext import db, admin, login_manager,migrate,api
from src.models import User, Category, Rubric, Video,Member,Message
from src.commands import populate_db,init_db
from src.endpoints.category.category import CategoryApi
from src.endpoints.rubric.rubric import RubricApi
from src.endpoints.video.video import VideoApi
from src.endpoints.member.member import MemberApi
from src.endpoints.message.message import MessageApi

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    register_extensions(app)
    
    return app

def register_extensions(app):
    db.init_app(app)
    login_manager.init_app(app)
    migrate.init_app(app,db)

    login_manager.login_view = 'admin.login_view'
    
 
    app.cli.add_command(init_db)
    app.cli.add_command(populate_db)

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))
    
    api.init_app(app)

    admin.init_app(app, index_view=SecureIndexView())

    admin.add_view(AdminUserView(User, db.session))
    admin.add_view(CategoryView(Category, db.session))
    admin.add_view(RubricView(Rubric, db.session))
    admin.add_view(VideoView(Video, db.session))
    admin.add_view(MemberView(Member, db.session))
    admin.add_view(MessageView(Message, db.session))

 