from src.admin.base import SecureModelView
from src.config import Config
from flask_admin.form.upload import ImageUploadField
from flask import redirect, url_for
from src.models import Image



class ProductView(SecureModelView):
    
    can_view_details = True
    edit_modal = True
    create_modal = True
    can_create = True
    can_edit = True
    can_export = True

    column_filters = ["title", "price"]
    column_default_sort = ("title", True)
    column_list = ["title", "price", "description", "images"]
    form_columns = ["title", "price", "description", "images"]
    column_sortable_list = ["title", "price"]
    column_searchable_list = ["title", "price"]
    column_labels = {
        "title": "სათაური",
        "price": "ფასი",
        "description": "აღწერა",
        "images": "ფოტოები",
    }
    
    inline_models = [(Image, {
        'form_overrides': {
            'filename': ImageUploadField
        },
        'form_args': {
            'filename': {
                'base_path': Config.UPLOAD_PATH
            }
        }
    })]

    