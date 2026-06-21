from flask_restx import fields
from flask_restx.reqparse import RequestParser

from src.ext import api


# category_delete_parser = RequestParser()
# category_delete_parser.add_argument('id',type=int,required = True )


category_model = api.model('category', {
                'id': fields.Integer,
                'category': fields.String
            })
#ამის გარეშეც შეიძლება