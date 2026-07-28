
from flask_restx import fields,inputs
from flask_restx.reqparse import RequestParser
from email_validator import validate_email,EmailNotValidError

from src.ext import api

message_model = api.model('message', {
    'id': fields.Integer(),
    'name': fields.String(),
    'surname': fields.String(),
    'text': fields.String(),
    'email': fields.String(),
    'phone_number': fields.String(),
    'company': fields.String(),
    'company_text': fields.String()
})

def check_email(email):
    try:
        valid_email= validate_email(email,check_deliverability=False)
        return valid_email.normalized
    except EmailNotValidError as e:
        raise ValueError(f'ელფოსტის არასწორი ფორმატი {e}')


message_parser = RequestParser()
message_parser.add_argument('name',type=str,required = True,trim=True,help='სახელი')
message_parser.add_argument('surname',type=str,required = True,trim=True,help='გვარი')
message_parser.add_argument('text',type=str,required = True,trim=True,help='ტექსტი')
message_parser.add_argument('email',type=check_email,required = True,trim=True,help='email')
message_parser.add_argument('phone_number',type=str,required = False,trim=True,help='ტელეფონის ნომერი')
message_parser.add_argument('company',type=str,required = False,trim=True,help='კომპანიის სახელი')
message_parser.add_argument('company_text',type=str,required = False,trim=True,help='კომპანიის ტექსტი')
