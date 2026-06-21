
from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,PasswordField
from wtforms.validators import DataRequired,ValidationError
from werkzeug.security import check_password_hash
from src.models import User

class LoginForm(FlaskForm):
    username = StringField('სახელი,გვარი', validators=[DataRequired()])
    password = PasswordField('პაროლი',validators=[DataRequired()])
    submit = SubmitField('შესვლა')

        
    def validate_password(self,field):
        user = User.query.filter_by(username = self.username.data).first()
        
        if not user or not check_password_hash(user._password,field.data):
            raise ValidationError('არასწორი სახელი ან პაროლი')
        
        self.user=user

0