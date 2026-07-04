from src.admin_views import SecureModelView
from markupsafe import Markup
from flask_admin.form import ImageUploadField
from os import path

from src.admin_views import generate_unique_name
from flask_admin.model.template import macro


class MemberView(SecureModelView):
    can_create = True
    can_delete = True
    can_edit = True
  

    column_list = ['img','name_surname','role','in_link']

    column_filters = ['name_surname','role','in_link']

    column_formatters = {
        'img': lambda v, c, m, p: Markup(
            f'<img src="/static/uploads/members/{m.img}" width="50" style="border-radius: 4px;">'
        )
    }
  

    form_extra_fields = {
                'img':ImageUploadField(
                base_path=path.join(path.dirname(__file__), '../static/uploads/members'),
                namegen=generate_unique_name)
                }



    

        
    
  
