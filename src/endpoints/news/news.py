from flask_restx import  Resource
import math
from src.ext import api
from src.models import News,Category
from src.endpoints.news import news_filter_parser,news_response_model
from src.models.tag import Tag
from src.models.type import Type

@api.route('/news')
class NewsApi(Resource):

    @api.expect(news_filter_parser)
    @api.marshal_with(news_response_model)
    def get(self):
        args = news_filter_parser.parse_args()
        category_name = args.get('category')
        title=args.get('title')
        tag_filter=args.get('tag')
        type_filter=args.get('type')
        uploaded_filter = args.get('uploaded_at')
        start_news=args.get('start_news')
        end_news=args.get('end_news')
        duration_filter = args.get('duration')
        page = args.get('page')
        per_page = args.get('per_page')

        news = News.query

        if category_name:
            category_filter = Category.query.filter(Category.category.ilike(f"%{category_name}%")).first()
            if category_filter:
                news = news.filter(News.category_id==category_filter.id)
            else:
                return {
                    'items':[],
                     'pagination_info':{
                          'page':page,
                          'per_page':per_page,
                          'total':0,
                          'total_pages':0                       
                     }},200
        if title:
                    news=news.filter(News.title.ilike(f"%{title}%"))
            
        if tag_filter:
            tag_list = [t.strip() for t in tag_filter.split(",")]
            for tag_name in tag_list:
                 news = news.filter(News.tag.any(Tag.name.ilike(f"%{tag_name}%")))

        if type_filter:
              news=news.filter(News.type.has(Type.name.ilike(f"%{type_filter}%")))

        if uploaded_filter:
             news = news.filter(News.uploaded_at>= uploaded_filter)

        if start_news and end_news:
             start_time = f"00:{int(start_news):02d}:00"
             end_time = f"00:{int(end_news):02d}:00"
             news=news.filter(News.duration.between(start_time,end_time))

        if  duration_filter:
             duration_format = f"00:{int(duration_filter):02d}:00"
             news = news.filter(News.duration==duration_format)
            
        current_page = page 
        pagination= news.paginate(page=current_page,per_page=per_page,error_out=False)
        return {
            "items": pagination.items,
            "pagination_info": {
            "page": current_page,
            "per_page": per_page,
            "total": pagination.total,
            "total_pages": math.ceil(pagination.total / per_page) if per_page else 0
            }
            }, 200
    
 
