from flask import Blueprint, render_template


info = Blueprint(
  "info",
  __name__,
  template_folder="templates",
  static_folder="static",
)


@info.route("/")
def index():
  return render_template("info/index.html")