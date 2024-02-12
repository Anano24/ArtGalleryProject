from flask import render_template, Blueprint


about_blueprint = Blueprint("about", __name__)



@about_blueprint.route("/about/")
def about_page():
    return render_template("about/about.html")
