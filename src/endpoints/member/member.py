from flask_restx import Resource

from src.ext import api
from src.models import Member
from src.endpoints.member import member_model

@api.route('/member')
class MemberApi(Resource):
    @api.marshal_with(member_model,as_list=True)
    def get(self):
        members = Member.query.all()
        return members