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
    df = create_final_dataset()
    print(df.head(3))
    print(df.values.tolist())
    return render_template('dataset.html', user=user, dataset=df.values.tolist())


def create_final_dataset():
    engine = create_engine(
        'postgresql://ktbzsdryoagyfd:77e6db1cf7aeff73105c60b05327baab2510216f8fb7736f9f8b36cf005a284b@ec2-44-195-100-240.compute-1.amazonaws.com:5432/dem8vtnut4f7km',
        echo=True)
    connection = engine.raw_connection()
    query = 'SELECT tagging.id, tagging.scraped_id, scraped.text, tagging.tagger, tagging.tagged_date, scraped.label FROM tagging INNER JOIN scraped ON scraped.id = tagging.scraped_id'
    df = pd.read_sql(query, con=connection, index_col="id")
    return df
