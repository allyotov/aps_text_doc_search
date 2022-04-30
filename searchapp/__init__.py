import logging
import os

from flask import Flask

from searchapp.resources.models import db
# from searchapp.resources.routes.routes import routes

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DB_URL']
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)
    # app.register_blueprint(routes, url_prefix='/api/v1/text_docs/')
    return app
