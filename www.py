from flask_cors import CORS

from app.home.index import home
from application import app

cors = CORS(app, resources={r"/apis/v1/*": {"origins": "*"}})

app.register_blueprint(home, url_prefix='/')
