from flask import Blueprint

home = Blueprint('index', __name__)


@home.route('/')
def index():
    return 'hello flask'
