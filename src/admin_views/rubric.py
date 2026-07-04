
from flask_admin.form import ImageUploadField
from uuid import uuid4
from os import path
from markupsafe import Markup
from src.admin_views import SecureModelView

def generate_unique_name(obj,file):
    extension = path.splitext(file.filename)[1]
    return f"{uuid4()}{extension}"

class RubricView(SecureModelView):
    can_create = True
    can_edit = True
    can_delete = True
    can_view_details = True


    form_extra_fields = {
            'img':ImageUploadField(
             base_path=path.join(path.dirname(__file__), '../static/uploads/rubrics'),
             namegen=generate_unique_name)
            }
    
    column_list = ['img','title' ,'description','uploaded_at']
    column_filters = ['title' ,'description','uploaded_at']

    column_formatters = {
        'img': lambda v, c, m, p: Markup(
            f'<img src="/static/uploads/rubrics/{m.img}" width="50" style="border-radius: 4px;">'
        )
    }
  




   
