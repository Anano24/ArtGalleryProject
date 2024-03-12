from src.admin.base import SecureModelView
from src.config import Config
from flask_admin.form.upload import ImageUploadField




class GalleryView(SecureModelView):
    can_view_details = True
    edit_modal = True
    create_modal = True
    can_create = True
    can_edit = True
    can_export = True


    column_filters = ["title"]

    column_default_sort = ("title", True)

    column_list = [
        "title",
        "description",
        "img",
    ]


    form_columns = [
        "title",
        "description",
        "img",
    ]

    form_overrides = {"img": ImageUploadField}

    form_args = {"img": {"base_path": Config.UPLOAD_PATH, "url_relative_path": "img/"}}

    column_sortable_list = [
        "title",
    ]

    column_searchable_list = [
        "title",
    ]

    column_labels = {
        "title": "სათაური",
        "description": "აღწერა",
        "img": "ფოტოები",
    }