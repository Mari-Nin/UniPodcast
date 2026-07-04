from datetime import datetime
from flask_restx import fields
from flask_restx.reqparse import RequestParser

from src.ext import api



rubric_filter_parser = RequestParser()
rubric_filter_parser.add_argument('category',type=str,help='Filter by category_name')
rubric_filter_parser.add_argument('page',type=int,default=1,help='Page number for pagination')
rubric_filter_parser.add_argument('per_page',type=int,default =5,help='Number of items per page')


rubric_model = api.model('rubric', {
                'id': fields.Integer,
                'title': fields.String,
                'img': fields.String,
                'description': fields.String,
                'duration': fields.String,
                'uploaded_at': fields.Date,
                'category_id': fields.Integer

            })
