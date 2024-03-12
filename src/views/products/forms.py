from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms.fields import StringField, IntegerField, SubmitField, TextAreaField
from wtforms.validators import DataRequired
from wtforms import StringField, IntegerField, TextAreaField, FormField, FieldList
from flask_admin.form.upload import ImageUploadField



class AddProductForm(FlaskForm):
    images = FileField('ატვირთეთ პროდუქტის სურათი', validators=[FileRequired()])
    # images = FileField('Images', validators=[FileRequired(), FileAllowed(['jpg', 'png', 'jpeg'], 'Images only!')])
    title = StringField('პროდუქტის სახელი', validators=[DataRequired()])
    price = IntegerField('პროდუქტის ფასი', validators=[DataRequired()])
    description = TextAreaField('აღწერა')
    submit = SubmitField('Add', validators=[DataRequired()])


# class ImageForm(FlaskForm):
#     filename = ImageUploadField('Image')

# class ProductForm(FlaskForm):
#     title = StringField('Title')
#     price = IntegerField('Price')
#     description = TextAreaField('Description')
#     images = FieldList(FormField(ImageForm))