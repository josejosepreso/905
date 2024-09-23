from flask import Blueprint, render_template

user = Blueprint("user", __name__)

@user.route("/home")
def home():
    return render_template("home.html");
