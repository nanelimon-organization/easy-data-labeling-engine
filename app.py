import os
import time

from flask import Flask

from models.models import db as models_db
from views.views import tagging_operations

app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
app.register_blueprint(tagging_operations)
models_db.init_app(app)


def setting():
    uri = os.getenv("DATABASE_URL")
    if uri.startswith("postgres://"):
        uri = uri.replace("postgres://", "postgresql://", 1)
        app.config['SQLALCHEMY_DATABASE_URI'] = uri
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SESSION_TYPE'] = 'filesystem'
    app.secret_key = "cokgizlibiranahtar"

    with app.app_context():
        models_db.create_all()




