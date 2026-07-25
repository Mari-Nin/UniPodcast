from datetime import datetime
from flask_restx import fields
from flask_restx.reqparse import RequestParser

from src.ext import api



news_filter_parser = RequestParser()
news_filter_parser.add_argument('category',type=str,help='Filter by category_name')
news_filter_parser.add_argument('title',type=str,help = 'Filter by news_title')
news_filter_parser.add_argument('tag',type=str,help="Filter news by ty tag,,example: tag1, tag2,tag3'")
news_filter_parser.add_argument('type',type=str, help = 'Filter news by type')
news_filter_parser.add_argument('uploaded_at',type= str,help = 'YYYY-MM-DD required format')
news_filter_parser.add_argument('start_news',type=str,help='Filter news by min_duration ')
news_filter_parser.add_argument('end_news',type=str,help='Filter news by max_duration ')
news_filter_parser.add_argument('duration',type=str,help='Filter news by duration ')
news_filter_parser.add_argument('page',type=int,default=1,help='Page number for pagination')
news_filter_parser.add_argument('per_page',type=int,default =5,help='Number of items per page')


news_model = api.model('news', {
                'id': fields.Integer,
                'category':fields.String,
                'title': fields.String,
                'tag':fields.String,
                'type':fields.String,
                'img': fields.String,     
                'description': fields.String,
                'duration': fields.String,
                'news_link':fields.String,
                'uploaded_at': fields.Date,
                'category_id': fields.Integer

            })

pagination_model = api.model('PaginationInfo',
                {
                'page': fields.Integer,
                'per_page': fields.Integer,
                'total': fields.Integer,
                'total_pages': fields.Integer
                })
news_response_model = api.model('News',
                {
                'items': fields.List(fields.Nested(news_model)),
                'pagination_info': fields.Nested(pagination_model)
                })
