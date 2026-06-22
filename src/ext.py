from flask_sqlalchemy import SQLAlchemy
from flask_admin import Admin,AdminIndexView
from flask_login import LoginManager
from flask_restx import Api
from flask_migrate import Migrate



db = SQLAlchemy()
login_manager = LoginManager()

class HomeAdminIndexView(AdminIndexView):
    def is_visible(self):
        return False
admin = Admin(name = 'Admin Page',index_view=HomeAdminIndexView())


migrate=Migrate()
api=Api(prefix='/api',doc='/api/docs')
