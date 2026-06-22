
from flask_restx import fields,inputs
from flask_restx.reqparse import RequestParser

from src.ext import api

video_filter_parser = RequestParser()
video_filter_parser.add_argument('category',type=str,help='Filter by category')
video_filter_parser.add_argument('time',type=str,help='Filter by duration ')
video_filter_parser.add_argument('page',type=int,default=1,help='page filter')
video_filter_parser.add_argument('next',type=int,default =5,help='>')

# rubric_filter_parser.add_argument('next',type=int,required = False,default =1,help='<')


video_model = api.model('video', {
                'id': fields.Integer,
                'title': fields.String,
                'img': fields.String,
                'description': fields.String,
                'guests': fields.String,
                'duration': fields.String,
                'uploaded_at': fields.Date,
                'in_slider': fields.Integer,
                'category_id': fields.Integer

            })
