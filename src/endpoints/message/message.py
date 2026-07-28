from flask_restx import Resource
from src.ext import api

from src.ext import db
from src.models import Message
from src.endpoints.message import message_model,message_parser

def check_input_data(data,field_data,min_length=2,max_length=50):
    if len(data) <min_length:
        api.abort (400, f'{field_data}->შეიყვანეთ მინიმუმ {min_length} სიმბოლო')
    elif len(data)>max_length:
        api.abort(400, f'{field_data}->დასაშვებია მაქსიმუმ {max_length} სიმბოლო')
    else:
        return data


@api.route('/message')
class MessageApi(Resource):

    @api.expect(message_parser)
    @api.marshal_with(message_model)
    def post(self):
        args = message_parser.parse_args()
        new_message = Message(
            name = check_input_data(args['name'], 'name'),
            surname = check_input_data(args['surname'], 'surname'),
            text = check_input_data(args['text'], 'text', min_length=5, max_length=200),
            phone_number = args.get('phone_number'),
            email = check_input_data(args['email'], 'email'),
            company = check_input_data(args.get('company'), 'company'),
            company_text = check_input_data(args.get('company_text'), 'company_text', min_length=5, max_length=200)
        )
                            
        db.session.add(new_message)
        db.session.commit()

        return new_message
        
    

