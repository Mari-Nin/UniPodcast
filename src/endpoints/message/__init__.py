
from flask_restx import fields
from flask_restx.reqparse import RequestParser

from src.ext import api

message_model=api.model('message',{
                        'id':fields.Integer,
                        'name':fields.String,
                        'surname':fields.String,
                        'text':fields.String,
                        'phone_number':fields.String,
                        'company':fields.String,
                        'company_text':fields.String

                                })
message_parser = RequestParser()
message_parser.add_argument('name',type=str,required = True,help='სახელი')
message_parser.add_argument('surname',type=str,required = True,help='გვარი')
message_parser.add_argument('text',type=str,required = True,help='ტექსტი')
message_parser.add_argument('phone_number',type=str,required = False,help='ტელეფონის ნომერი')
message_parser.add_argument('company',type=str,required = False,help='კომპანიის სახელი')
message_parser.add_argument('company_text',type=str,required = False,help='კომპანიის ტექსტი')
