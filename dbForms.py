from wtforms import Form, StringField, TextAreaField,PasswordField,validators
from wtforms.validators import InputRequired, Email
from werkzeug.security import check_password_hash,generate_password_hash



class UserRegister(Form):
    username = StringField("Username:", validators= [validators.Length(min=6, max=30)])
    email = StringField("Email:", [InputRequired("Please enter your email address."), Email("This field requires a valid email address")])
    password = PasswordField("Password:",validators=[validators.InputRequired()])

class LoginUser(Form):
    username = StringField("Username:")
    password = PasswordField("Password:")
    
   
