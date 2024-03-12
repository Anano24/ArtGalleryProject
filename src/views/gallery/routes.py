
from flask import render_template, redirect, url_for, Blueprint
from flask_login import login_required
from uuid import uuid4
import os

from src.models import GalleryItem
from src.views.gallery.forms import AddGalleryItemForm
from src.config import Config
from src.extentions import db


gallery_blueprint = Blueprint("gallery", __name__)


@gallery_blueprint.route('/gallery')
def gallery_page():
    gallery_items = GalleryItem.query.all()
    return render_template('gallery/gallery.html', gallery_items=gallery_items)



@gallery_blueprint.route('/edit_gallery/<int:id>', methods=["GET", "POST"])
def edit_gallery(id):
    gallery_item = GalleryItem.query.get(id)
    form = AddGalleryItemForm(obj=gallery_item)

    if form.validate_on_submit():
        # Update product attributes from form data
        gallery_item.title = form.title.data
        gallery_item.description = form.description.data

        # Upload file if a new one is provided
        file = form.img.data
        if file:
            filename, filetype = file.filename.split(".")
            filename = str(uuid4())
            directory = os.path.join(Config.UPLOAD_PATH, f"{filename}.{filetype}")
            file.save(directory)
            gallery_item.img = f"{filename}.{filetype}"

        gallery_item.create()
        return redirect(url_for('gallery.gallery_page'))

    return render_template('gallery/edit_gallery_item.html', form=form)


