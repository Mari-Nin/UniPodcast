from flask import render_template, url_for, redirect, request
from flask_admin import expose, AdminIndexView
from flask_admin.contrib.sqla import ModelView

from flask_login import current_user, login_user, logout_user

from src.admin_views.forms import LoginForm


class SecureModelView(ModelView):
    def is_accessible(self):
        return current_user.is_authenticated and current_user.role == 'admin'

    def inaccessible_callback(self, name, **kwargs):
        return redirect(url_for('admin.login_view', next=request.url))


class SecureIndexView(AdminIndexView):

    def is_accessible(self):
        if '/admin/login/' in request.path:
            return True
        return current_user.is_authenticated and current_user.role == 'admin'

    def inaccessible_callback(self, name, **kwargs):
        return redirect(url_for('admin.login_view', next=request.url))

    @expose('/')
    def index(self):
        return super(SecureIndexView, self).index()


    @expose('/login/', methods=["GET", "POST"])
    def login_view(self):
        form = LoginForm()

        if current_user.is_authenticated and current_user.role == 'admin':
            return redirect(url_for('.index'))

        if form.validate_on_submit():
            if form.user and form.user.role =='admin':
                login_user(form.user)
                next_page = request.args.get('next')
                return redirect(next_page or url_for('.index'))
            else:
                return redirect('/')
            
        return render_template('login.html', form=form)

    @expose('/logout')
    def logout_view(self):
        logout_user()
        return redirect(url_for('.login_view'))
        # return redirect('/admin/login/')