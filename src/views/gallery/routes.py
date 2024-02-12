from flask import render_template, Blueprint


gallery_blueprint = Blueprint("gallery", __name__)


@gallery_blueprint.route('/gallery')
def gallery_page():
    # products = Product.query.all()
    return render_template('gallery/gallery.html')


