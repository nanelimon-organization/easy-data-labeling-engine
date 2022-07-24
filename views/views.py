from flask import Blueprint, render_template, flash

from models.models import Tagging


tagging_operations = Blueprint('tagging_operations', __name__)


@tagging_operations.route('/', methods=['GET'])
def index():
    query = Tagging.query.filter_by(label=True).all()
    warning = None
    if len(query) < 1:
        warning = 'Bütün Tweetler Etiketlendi!'
    return render_template('index.html', text=query, warning=warning)
