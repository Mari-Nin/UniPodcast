from flask_restx import  Resource

from src.ext import api
from src.models import Category
from src.endpoints.category import category_model   #category_delete_parser


@api.route('/category')
class CategoryApi(Resource):

    @api.marshal_with(category_model)
    def get(self):
        categories = Category.query.all()
        return categories,200
    

    
    # @api.doc(parser = category_delete_parser)
    # def delete(self):
    #     args = category_delete_parser.parse_args()
    #     category_delete = Category.query.get(args['id'])
    #     if not category_delete:

    #         return f"Category with ID N {args['id']} does not exist", 404
    #     category_delete.delete()

    #     return f"Category with ID N {args['id']} is deleted", 201
