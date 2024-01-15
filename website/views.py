from flask import Blueprint

# Blueprint of the application
views = Blueprint('views', __name__)

@views.route('/')
def home():
    return "<h1>Test</h1>"