import os
from flask import Flask
from flask_session import Session
from models.models import db as models_db
from views.views import tagging_operations


app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))

app.secret_key = "cokgizlibiranahtar"

"""app.config['SQLALCHEMY_DATABASE_URI'] = \
    'sqlite:///' + os.path.join(basedir, 'database.db')"""

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://ktbzsdryoagyfd:77e6db1cf7aeff73105c60b05327baab2510216f8fb7736f9f8b36cf005a284b@ec2-44-195-100-240.compute-1.amazonaws.com:5432/dem8vtnut4f7km'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SESSION_TYPE'] = 'filesystem'
Session(app)

app.register_blueprint(tagging_operations)
models_db.init_app(app)


with app.app_context():
    models_db.create_all()
