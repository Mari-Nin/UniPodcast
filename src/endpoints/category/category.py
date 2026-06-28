from flask_restx import  Resource

from src.ext import api
from src.models import Category
from src.endpoints.category import category_model   


@api.route('/category')
class CategoryApi(Resource):

    @api.marshal_with(category_model,as_list=True)
    def get(self):
        categories = Category.query.all()
        return categories,200
    

    
    