from flask_restx import Resource
from src.ext import api

from src.ext import db
from src.models import Message
from src.endpoints.message import message_model,message_parser



@api.route('/message')
class MessageApi(Resource):

    @api.expect(message_parser)
    @api.marshal_with(message_model)
    def post(self):
        args = message_parser.parse_args()
        new_message = Message(
                    name = args['name'],
                    surname = args['surname'],
                    text = args['text'],
                    phone_number = args.get('phone_number'),
                    company=args.get('company'),
                    company_text=args.get('company_text')
                     )
        db.session.add(new_message)
        db.session.commit()

        return new_message

    

