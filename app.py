import os
from flask import Flask

from models.models import db as models_db
from views.views import tagging_operations


app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))

app.secret_key = "cokgizlibiranahtar"

"""app.config['SQLALCHEMY_DATABASE_URI'] = \
    'sqlite:///' + os.path.join(basedir, 'database.db')"""
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://Imcseyma_seymas:Ep969p7X@93.89.225.181/Imcseyma_db_nan'


app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SESSION_TYPE'] = 'filesystem'

app.register_blueprint(tagging_operations)
models_db.init_app(app)


with app.app_context():
    models_db.create_all()
