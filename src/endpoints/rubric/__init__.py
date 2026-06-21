from datetime import datetime
from flask_restx import fields
from flask_restx.reqparse import RequestParser

from src.ext import api


# rubric_delete_parser = RequestParser()
# rubric_delete_parser.add_argument('id',type=int,required = True )

rubric_filter_parser = RequestParser()
rubric_filter_parser.add_argument('category',type=str,help='Filter by category')
rubric_filter_parser.add_argument('page',type=int,default=1,help='page filter')
rubric_filter_parser.add_argument('next',type=int,default =5,help='>')

# rubric_filter_parser.add_argument('next',type=int,required = False,default =1,help='<')


rubric_model = api.model('rubric', {
                'id': fields.Integer,
                'title': fields.String,
                'img': fields.String,
                'description': fields.String,
                'duration': fields.String,
                'uploaded_at': fields.Date,
                'category_id': fields.Integer

            })
