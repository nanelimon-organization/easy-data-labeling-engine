from decouple import config
import os
from flask import Flask
from models.models import db as models_db
from views.views import tagging_operations

app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))

app.secret_key = config('secret_key')

app.config['SQLALCHEMY_DATABASE_URI'] = \
    'sqlite:///' + os.path.join(basedir, 'database.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SESSION_TYPE'] = 'filesystem'

app.register_blueprint(tagging_operations)
models_db.init_app(app)

with app.app_context():
    models_db.create_all()

if __name__ == "__main__":
    app.run()
