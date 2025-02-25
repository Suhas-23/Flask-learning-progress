from flask import Blueprint, render_template

main = Blueprint('main', __name__)


@main.route('/')
def home():
    return "Welcome to the Main Page!"


@main.route('/about')
def about():
    return render_template('about.html')
