import pandas as pd
from flask import Blueprint, render_template, redirect

import getpass

from sqlalchemy import create_engine

from models.models import Tagging, Scraped
from flaskthreads import AppContextThread

tagging_operations = Blueprint('tagging_operations', __name__)
user = getpass.getuser()


@tagging_operations.route('/', methods=['GET'])
def index():
    query = Scraped.query.filter(Scraped.tagging_status == False).all()
    warning = None
    if len(query) < 1:
        warning = 'Bütün Tweetler Etiketlendi!'
    return render_template('index.html', text=query, warning=warning, user=user)


@tagging_operations.route('/bullying/<string:selected>/<int:id>')
def label_as_bully(id, selected):
    Scraped.label_update(id=id, label=selected, tagging_status=True)
    Tagging.new_data_insert(scraped_id=id, tagger=getpass.getuser())
    return redirect('/')


@tagging_operations.route('/not_bulling/<int:id>')
def label_as_not_bully(id):
    Scraped.label_update(id=id, label='Nötr', tagging_status=True)
    Tagging.new_data_insert(scraped_id=id, tagger=getpass.getuser())
    return redirect('/')


@tagging_operations.route('/delete/<int:id>')
def delete(id):
    # Zorbalık yok ama Tagging datasına(yani nihayi datasete) dahil edilmeyecek.
    Scraped.label_update(id=id, label='Sil', tagging_status=True)
    return redirect('/')


@tagging_operations.route('/extract_dataset')
def extract_dataset():
    query = Tagging.query\
            .join(Scraped)\
            .filter(Tagging.scraped_id == Scraped.id)
    print(query)
    return render_template('dataset.html', user=user, dataset=query)
