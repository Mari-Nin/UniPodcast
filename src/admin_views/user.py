

from src.admin_views import SecureModelView


class AdminUserView(SecureModelView):
    can_create = True
    can_edit = True
    can_delete = True

    column_exclude_list = ['_password']

    form_excluded_columns=['_password']
    
