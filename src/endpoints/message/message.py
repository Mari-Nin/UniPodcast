from flask_restx import Resource
from src.ext import api

from src.ext import db
from src.models import Message
from src.endpoints.message import message_model,message_parser

def check_length(data,min_length=2,max_length=50):
    if len(data) <min_length:
        api.abort (400, f'შეიყვანეთ მინიმუმ {min_length} სიმბოლო')
    elif len(data)>max_length:
        api.abort(400, f'დასაშვებია მაქსიმუმ {max_length} სიმბოლო')
    else:
        return data


@api.route('/message')
class MessageApi(Resource):

    @api.expect(message_parser)
    @api.marshal_with(message_model)
    def post(self):
        args = message_parser.parse_args()
        new_message = Message(
                    name = check_length(args['name']),
                    surname = check_length(args['surname']),
                    text = check_length(args['text'], min_length=5,max_length=200),
                    phone_number = args.get('phone_number'),
                    email = args['email'],
                    company=args.get('company'),
                    company_text=args.get('company_text')
                     )
        db.session.add(new_message)
        db.session.commit()

        return new_message
        
    

