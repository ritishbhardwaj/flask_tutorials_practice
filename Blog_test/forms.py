from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField
from wtforms.validators import DataRequired,Length,Email,EqualTo


class RegistrationForm(FlaskForm):
    
    username= StringField('Username',
                          validators=[DataRequired(),Length(min=2,max=20)])      #here DataRequired is a class so it is important to put paranthesis after declaring the class 
    
    email=StringField('Email',
                      validators=[DataRequired(),Email()])
    
    password=PasswordField('Password',validators=[DataRequired(),Length(min=3,max=30)])
    
    confirm_password=PasswordField('Confirm Password',validators=[DataRequired(),EqualTo('password')])
    
    
    submit = SubmitField('Sign Up')
    
    
from wtforms import BooleanField

class LoginForm(FlaskForm):
    
    email=StringField('Email',
                      validators=[DataRequired(),Email()])
    
    password=PasswordField('Password',validators=[DataRequired(),Length(min=3,max=30)])
    # confirm_password=PasswordField('Confirm Password',validators=[DataRequired(),EqualTo('password')])
    
    remember = BooleanField('Remember Me')
    submit = SubmitField('Sign Up')