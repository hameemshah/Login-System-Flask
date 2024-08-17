from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, EmailField, PasswordField
from wtforms.validators import DataRequired, Email, Length, EqualTo

class LoginForm(FlaskForm):
    email = EmailField(validators=[DataRequired()])
    password = PasswordField(validators=[DataRequired(), Length(min=6, message="Minimum six characters")])
    submit = SubmitField('Login')

class SignupForm(FlaskForm):
    username = StringField(validators=[DataRequired(), Length(max=10)])
    email = EmailField(validators=[DataRequired()])
    password = PasswordField(validators=[DataRequired(), Length(min=6, message="Minimum six characters")])
    confirm = PasswordField("Confirm Password", validators=[DataRequired(), Length(min=6, message="Minimum six characters"), EqualTo('password', "Password should be same")])
    submit = SubmitField('Sign Up')