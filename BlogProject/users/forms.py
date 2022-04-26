### BlogProject/users/forms.py

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo
from wtforms import ValidationError

### filefield and fileallowed allows users to upload a jpeg or png file
from flask_wtf.file import FileField,FileAllowed

## users
from flask_login import current_user
from BlogProject.models import User

## LogIn Form
class LoginForm(FlaskForm):

    email = StringField('Email',validators=[DataRequired(),Email()])
    password = PasswordField('Password',validators=[DataRequired()])
    submit = SubmitField('Log In')

## Registration Form
class RegistrationForm(FlaskForm):

    email = StringField('Email',validators=[DataRequired(),Email()])
    username = StringField('UserName',validators=[DataRequired()])

    ## use EqualTo to match the both passwords
    password = PasswordField('Password',validators=[DataRequired(), EqualTo('pass_confirm', message = 'Passwords must match')])
    pass_confirm = PasswordField('Confirm Password',validators=[DataRequired()])

    submit = SubmitField('Register')

    ## check email is not used by any other user - no duplicates
    def check_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('Your email has been registered already!')

    ## check unique user names
    def check_username(self, field):
        if User.query.filter_by(usernamel=field.data).first():
            raise ValidationError('Your username has been registered already!')

### updating the user details
class UpdateUserForm(FlaskForm):

    email = StringField('Email',validators=[DataRequired(),Email()])
    username = StringField('UserName',validators=[DataRequired()])
    picture = FileField('Update Profile Picture',validators = [FileAllowed(['jpg', 'png'])])
    submit = SubmitField('Submit')

    ## check email is not used by any other user - no duplicates
    def check_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('Your email has been registered already!')

    ## check unique user names
    def check_username(self, field):
        if User.query.filter_by(usernamel=field.data).first():
            raise ValidationError('Your username has been registered already!')