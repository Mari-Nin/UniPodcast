from os import path

class Config():

    SECRET_KEY = 'adminadminunipodcast'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + path.join(path.dirname(__file__),'test.db')
    UPLOAD_PATH = path.join(path.dirname(__file__), 'static')