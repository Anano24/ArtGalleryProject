from src.admin.base import SecureModelView
from src.config import Config
from flask_admin.form.upload import ImageUploadField




class ProductView(SecureModelView):
    can_view_details = True
    edit_modal = True
    create_modal = True
    can_create = True
    can_edit = True
    can_export = True


    column_filters = ["title", "price"]

    column_default_sort = ("title", True)

    column_list = [
        "title",
        "price",
        "description",
        "images",
    ]

    # def _list_formatter(view, context, model, name):
    #     """Format images as a list of filenames."""
    #     return ', '.join([image.filename for image in model.images])

    # column_formatters = {
    #     'formatted_images': _list_formatter
    # }


    form_columns = [
        "title",
        "price",
        "description",
        "images",
    ]

    form_overrides = {"images": ImageUploadField}

    form_args = {"images": {"base_path": Config.UPLOAD_PATH, "url_relative_path": "img/"}}

    column_sortable_list = [
        "title",
        "price",
    ]

    column_searchable_list = [
        "title",
        "price",
    ]

    column_labels = {
        "title": "სათაური",
        "price": "ფასი",
        "description": "აღწერა",
        "images": "ფოტოები",
    }