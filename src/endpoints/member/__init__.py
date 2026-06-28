from flask_restx import fields

from src.ext import api

member_model = api.model('member', {
                'id': fields.Integer,
                'name_surname': fields.String,
                'role':fields.String,
                'in_link':fields.String,
                'img':fields.String

            })
