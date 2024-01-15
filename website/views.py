from flask import Blueprint, render_template

# Blueprint of the application
views = Blueprint('views', __name__)

@views.route('/')
def home():
    return render_template("home.html")