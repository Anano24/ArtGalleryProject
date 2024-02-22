from flask import render_template, Blueprint

from src.models import Product


gallery_blueprint = Blueprint("gallery", __name__)


@gallery_blueprint.route('/gallery')
def gallery_page():
    gallery_items = Product.query.all()
    return render_template('gallery/gallery.html', products=gallery_items)


