from flask_admin.form import ImageUploadField
from uuid import uuid4
from os import path

from src.admin_views.rubric import generate_unique_name
# თავიდან რომ არ ვწერო ფუნქცია
from src.admin_views.base import SecureModelView


class VideoViews(SecureModelView):
     can_create = True
     can_edit = True
     can_delete = True

     form_extra_fields = {
            'img':ImageUploadField(
             base_path=path.join(path.dirname(__file__), '../static/uploads/videos'),
             namegen=generate_unique_name)
            }


    