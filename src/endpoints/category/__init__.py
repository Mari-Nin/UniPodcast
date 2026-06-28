from flask_restx import fields


from src.ext import api


category_model = api.model('category', {
                'id': fields.Integer,
                'category': fields.String
            })
