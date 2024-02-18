from flask import render_template, Blueprint

from src.models import GalleryItem


gallery_blueprint = Blueprint("gallery", __name__)


@gallery_blueprint.route('/gallery')
def gallery_page():
    gallery_items = GalleryItem.query.all()
    return render_template('gallery/gallery.html', gallery_items=gallery_items)


