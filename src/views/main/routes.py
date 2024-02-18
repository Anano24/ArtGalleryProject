from flask import render_template, Blueprint



main_blueprint = Blueprint("main", __name__)


@main_blueprint.route("/")
@main_blueprint.route("/home")
def home():
    return render_template("main/main.html")

