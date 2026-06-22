from flask_restx import  Resource

from src.ext import api
from src.models import Rubric,Category
from src.endpoints.rubric import rubric_model,rubric_filter_parser  #rubric_delete_parser,


@api.route('/rubric')
class RubricApi(Resource):

    @api.expect(rubric_filter_parser)
    @api.marshal_with(rubric_model)
    def get(self):
        args = rubric_filter_parser.parse_args()
        category_name = args.get('category')
        page = args.get('page')
        next_page = args.get('next',5)

        rubrics = Rubric.query
        if category_name:
            category_filter = Category.query.filter(Category.category==category_name).first()
            if category_filter:
                rubrics = rubrics.filter(Rubric.category_id==category_filter.id)
            else:
                return [],200

        if page:
            current_page = page
        else:
            current_page=1

        pagin_rubrics = rubrics.paginate(page=current_page,per_page=next_page,error_out=False)

        return pagin_rubrics.items,200
    
 
    
    # @api.doc(parser = rubric_delete_parser)
    # def delete(self):
    #     args = rubric_delete_parser.parse_args()
    #     rubric_delete = Rubric.query.get(args['id'])
    #     if not rubric_delete:
    #         return f'Rubric with ID N {args['id']} does not exist', 404
        
    #     rubric_delete.delete()

    #     return f'Rubric with ID  N {args['id']} is deleted',201
