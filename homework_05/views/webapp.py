from flask import (
    Blueprint,
    render_template,
)


webapp = Blueprint("webapp", __name__)


@webapp.get("/", endpoint="index")
def index_view():
    return render_template("app/index.html")


@webapp.get("/about/", endpoint="about")
def show_about():
    return render_template("app/about.html")

