
from flask_restx import  Resource
from sqlalchemy import cast,String

from src.ext import api
from src.models import Video,Category
from src.endpoints.video import video_filter_parser,video_model


@api.route('/video')
class VideoApi(Resource):

    @api.expect(video_filter_parser)
    @api.marshal_with(video_model,as_list=True)
    def get(self):
        args = video_filter_parser.parse_args()
        category_name = args.get('category')
        video_duration=args.get('duration')
        page = args.get('page')
        next_page = args.get('next',5)

        videos = Video.query
        if category_name:
            category_filter = Category.query.filter(Category.category==category_name).first()
            if category_filter:
                videos = videos.filter(Video.category_id==category_filter.id)
            else:
                return [],200
        if video_duration:
            videos = videos.filter(cast(Video.duration,String).like(f'%{video_duration}%') )

        if page:
            current_page = page
        else:
            current_page=1

        pagin_rubrics = videos.paginate(page=current_page,per_page=next_page,error_out=False)

        return pagin_rubrics.items,200


@api.route('/slider')
class SliderApi(Resource):
    @api.marshal_with(video_model,as_list = True)
    def get(self):
        slider_videos = Video.query.filter(Video.in_slider == True).all()
        return slider_videos
    
