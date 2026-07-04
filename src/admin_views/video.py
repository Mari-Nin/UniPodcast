from flask_admin.form import ImageUploadField
from uuid import uuid4
from markupsafe import Markup
from os import path

from src.admin_views import generate_unique_name
from src.admin_views.base import SecureModelView


class VideoView(SecureModelView):
     can_create = True
     can_edit = True
     can_delete = True
     can_view_details = True

     form_extra_fields = {
            'img':ImageUploadField(
             base_path=path.join(path.dirname(__file__), '../static/uploads/videos'),
             namegen=generate_unique_name)
            }
     
     column_list = ['img','title','description','guests','uploaded_at']

     column_filters = ['title','description','guests','uploaded_at']

     column_formatters = {
        'img': lambda v, c, m, p: Markup(
            f'<img src="/static/uploads/videos/{m.img}" width="50" style="border-radius: 4px;">'
        )
    }
  



    