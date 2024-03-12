from flask import render_template, Blueprint

from src.models import GalleryItem



main_blueprint = Blueprint("main", __name__)


@main_blueprint.route("/")
@main_blueprint.route("/home")
def home():
    gallery_items = GalleryItem.query.all()
    return render_template("main/main.html", gallery_items=gallery_items)
    

