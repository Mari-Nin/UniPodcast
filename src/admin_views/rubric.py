
from flask_admin.form import ImageUploadField
from uuid import uuid4
from os import path
from src.admin_views.base import SecureModelView

def generate_unique_name(obj,file):
    extension = path.splitext(file.filename)[1]
    return f"{uuid4()}{extension}"

class RubricView(SecureModelView):
    can_create = True
    can_edit = True
    can_delete = True



    form_extra_fields = {
            'img':ImageUploadField(
             base_path=path.join(path.dirname(__file__), '../static/uploads/rubrics'),
             namegen=generate_unique_name)
            }



   
