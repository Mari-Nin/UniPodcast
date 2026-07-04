from flask_restx import  Resource

from src.ext import api
from src.models import Rubric,Category
from src.endpoints.rubric import rubric_model,rubric_filter_parser 


@api.route('/rubric')
class RubricApi(Resource):

    @api.expect(rubric_filter_parser)
    @api.marshal_with(rubric_model)
    def get(self):
        args = rubric_filter_parser.parse_args()
        category_name = args.get('category')
        page = args.get('page')
        per_page = args.get('per_page')

        rubrics = Rubric.query
        if category_name:
            category_filter = Category.query.filter(Category.category==category_name).first()
            if category_filter:
                rubrics = rubrics.filter(Rubric.category_id==category_filter.id)
            else:
                return [],200

        current_page = page or 1

        pagin_rubrics = rubrics.paginate(page=current_page,per_page=per_page,error_out=False)

        return pagin_rubrics.items,200
    
 
