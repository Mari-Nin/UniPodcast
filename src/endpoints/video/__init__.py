
from flask_restx import fields
from flask_restx.reqparse import RequestParser

from src.ext import api

video_filter_parser = RequestParser()
video_filter_parser.add_argument('category',type=str,help='Filter  by category name')
video_filter_parser.add_argument('title',type=str,help = 'Filter by video title')
video_filter_parser.add_argument('tag',type=str,help='Filter by video tag')
video_filter_parser.add_argument('type',type=str,help='Filter by video type,example: tag1, tag2,tag3')
video_filter_parser.add_argument('uploaded_at',type= str,help = 'YYYY-MM-DD required format')
video_filter_parser.add_argument('start_video',type=str,help='Filter videos by min_duration ')
video_filter_parser.add_argument('end_video',type=str,help='Filter videos by max_duration ')
video_filter_parser.add_argument('duration',type=str,help='Filter videos by duration ')
video_filter_parser.add_argument('page',type=int,default=1,help='Page number for pagination')
video_filter_parser.add_argument('per_page',type=int,default =5,help='Number of videos per page')

video_model = api.model('video', {
                'id': fields.Integer,
                'category':fields.String,
                'title': fields.String,
                'type':fields.String,
                'tag':fields.String,
                'img': fields.String,
                'description': fields.String,
                'guests': fields.String,
                'duration': fields.String,
                'uploaded_at': fields.Date,
                'video_link':fields.String,
                'in_slider': fields.Integer,
                'category_id': fields.Integer

            })
pagination_model = api.model("PaginationInfo", {
                    "page": fields.Integer,
                    "per_page": fields.Integer,
                    "total": fields.Integer,
                    "total_pages": fields.Integer
                                    })


videos_response_model = api.model('Videos',
                {
                'items': fields.List(fields.Nested(video_model)),
                'pagination_info': fields.Nested(pagination_model)
                })



