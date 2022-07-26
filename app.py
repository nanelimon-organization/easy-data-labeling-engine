import os
from flask import Flask

from models.models import db as models_db
from views.views import tagging_operations


app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))

app.secret_key = "cokgizlibiranahtar"

"""app.config['SQLALCHEMY_DATABASE_URI'] = \
    'sqlite:///' + os.path.join(basedir, 'database.db')"""
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://tfebtxzxlgssjc:41e1741c907c8fa23d960f7c99b53cc83688da12337f4565dde9d9e51c96f899@ec2-54-225-234-165.compute-1.amazonaws.com:5432/da5jjovb79fk6g'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SESSION_TYPE'] = 'filesystem'

app.register_blueprint(tagging_operations)
models_db.init_app(app)


with app.app_context():
    models_db.create_all()
