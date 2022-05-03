import logging
import os

from flask import Flask
from flask_swagger_ui import get_swaggerui_blueprint
from searchapp.resources.models import db
from searchapp.resources.routes.routes import routes


SWAGGER_URL = '/swagger'
API_URL = '/static/docs.json'
SWAGGERUI_BLUEPRINT = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': "post_search_app",
        'validatorUrl': None,
    }
)

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DB_URL']
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)
    app.register_blueprint(routes, url_prefix='/api/v1/text_docs/')
    app.register_blueprint(SWAGGERUI_BLUEPRINT, url_prefix=SWAGGER_URL)
    return app
