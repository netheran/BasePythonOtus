from flask import (
    Blueprint,
    render_template,
)


web_app = Blueprint("webapp", __name__)


@web_app.get("/", endpoint="index")
def index_view():
    return render_template("templates/app/index.html")


@web_app.get("/about/", endpoint="about")
def show_about():
    return render_template("templates/app/about.html")

