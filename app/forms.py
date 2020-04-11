from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, TextAreaField
from wtforms.validators import DataRequired, Email
from flask_wtf.file import FileField, FileRequired,FileAllowed


class UserProfileForm(FlaskForm):
    firstName = StringField('First Name', validators=[DataRequired()])
    lastName = StringField('Last Name', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    location = StringField('location', validators=[DataRequired()])
    gender = SelectField('Gender', validators=[DataRequired()], choices=[(0, "Male"), (1, "Female")])
    biography = TextAreaField('Biography', validators=[DataRequired()])
    photo = FileField('Profile Picture', validators=[FileRequired(), FileAllowed(['jpg', 'png'], 'Images only!')])
    