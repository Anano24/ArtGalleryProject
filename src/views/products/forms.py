from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired
from wtforms.fields import StringField, IntegerField, SubmitField
from wtforms.validators import DataRequired



class AddProductForm(FlaskForm):
    img = FileField('ატვირთეთ პროდუქტის სურათი', validators=[FileRequired()])
    title = StringField('პროდუქტის სახელი', validators=[DataRequired()])
    price = IntegerField('პროდუქტის ფასი', validators=[DataRequired()])
    submit = SubmitField('დამატება', validators=[DataRequired()])