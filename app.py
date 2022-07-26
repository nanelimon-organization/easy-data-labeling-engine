import os
from flask import Flask

from models.models import db as models_db
from views.views import tagging_operations


app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))

app.secret_key = "cokgizlibiranahtar"

"""app.config['SQLALCHEMY_DATABASE_URI'] = \
    'sqlite:///' + os.path.join(basedir, 'database.db')"""
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://scibriigaxirvh" \
                                        ":701e929c57a1042d3ac1c53aa27a433ca0c15541329106abe1a012d00be8d533@ec2-107-22" \
                                        "-122-106.compute-1.amazonaws.com:5432/d9i8pr0r2k38vf "

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SESSION_TYPE'] = 'filesystem'

app.register_blueprint(tagging_operations)
models_db.init_app(app)


"""with app.app_context():
    models_db.create_all()"""
