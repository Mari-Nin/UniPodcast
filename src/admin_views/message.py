from src.admin_views import SecureModelView

class MessageView(SecureModelView):
    can_create=False
    can_delete=False
    can_view_details=True


    column_list = ['name','surname','text','phone_number','seen']

    column_editable_list = ['name','surname','text','phone_number','seen']
    
    column_filters = ['name','surname','text','phone_number','seen']