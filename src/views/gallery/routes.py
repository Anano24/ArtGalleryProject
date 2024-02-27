
from flask import render_template, redirect, url_for, Blueprint
from flask_login import login_required
from uuid import uuid4
import os

from src.models import Product, Image
from src.views.products.forms import AddProductForm
from src.config import Config
from src.extentions import db


gallery_blueprint = Blueprint("gallery", __name__)


@gallery_blueprint.route('/gallery')
def gallery_page():
    gallery_items = Product.query.all()
    return render_template('gallery/gallery.html', products=gallery_items)



@gallery_blueprint.route('/edit_gallery/<int:id>', methods=["GET", "POST"])
def edit_gallery(id):
    product = Product.query.get(id)
    form = AddProductForm(obj=product)

    if form.validate_on_submit():
        # Update product attributes from form data
        product.title = form.title.data
        product.description = form.description.data
        product.price = form.price.data

        # Upload file if a new one is provided
        file = form.images.data
        if file:
            filename, filetype = file.filename.split(".")
            filename = str(uuid4())
            directory = os.path.join(Config.UPLOAD_PATH, f"{filename}.{filetype}")
            file.save(directory)

            for image in product.images:
                image.filename = f"{filename}.{filetype}"


        product.create()
        return redirect(url_for('gallery.gallery_page'))

    return render_template('gallery/edit_gallery_item.html', form=form)


