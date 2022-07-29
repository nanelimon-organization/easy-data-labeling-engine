import pandas as pd
from flask import Blueprint, render_template, redirect
import getpass

from sqlalchemy import create_engine

from models.models import Tagging, Scraped

tagging_operations = Blueprint('tagging_operations', __name__)
user = getpass.getuser()


@tagging_operations.route('/', methods=['GET'])
def index():
    query = Scraped.query.filter(Scraped.tagging_status == False).all()
    warning = None
    if len(query) < 1:
        warning = 'Bütün Tweetler Etiketlendi!'
    return render_template('index.html', text=query, warning=warning, user=user)


@tagging_operations.route('/bullying/<int:id>')
def label_as_bully(id):
    Scraped.label_update(id=id, label=True, tagging_status=True)
    Tagging.new_data_insert(scraped_id=id, tagger=getpass.getuser())
    return redirect('/')


@tagging_operations.route('/not_bulling/<int:id>')
def label_as_not_bully(id):
    Scraped.label_update(id=id, label=False, tagging_status=True)
    Tagging.new_data_insert(scraped_id=id, tagger=getpass.getuser())
    return redirect('/')


@tagging_operations.route('/delete/<int:id>')
def delete(id):
    #Zorbalık yok ama Tagging datasına(yani nihayi datasete) dahil edilmeyecek.
    Scraped.label_update(id=id, label=False, tagging_status=True)
    return redirect('/')


@tagging_operations.route('/extract_dataset')
def extract_dataset():
    engine = create_engine(
        'mysql+pymysql://Imcseyma_seymas:Ep969p7X@93.89.225.181/Imcseyma_db_nan',
        echo=True)
    connection = engine.raw_connection()
    query = "SELECT tagging.scraped_id, scraped.text, tagging.tagger, tagging.tagged_date, scraped.label FROM tagging INNER JOIN scraped ON scraped.id = tagging.scraped_id"
    df = pd.read_sql(query ,con=connection, index_col="scraped_id")
    df.to_csv('static/datas/dataset.csv')
    return redirect('/')

