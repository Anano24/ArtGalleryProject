from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired
from wtforms.fields import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired



class AddGalleryItemForm(FlaskForm):
    img = FileField('ატვირთეთ პროდუქტის სურათი', validators=[FileRequired()])
    title = StringField('პროდუქტის სახელი', validators=[DataRequired()])
    description = TextAreaField('აღწერა')
    submit = SubmitField('Add', validators=[DataRequired()])