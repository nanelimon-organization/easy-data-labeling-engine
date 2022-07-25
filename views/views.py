import datetime

from flask import Blueprint, render_template, redirect
import getpass

from models.models import Tagging, Scraped,db

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
    Scraped.label_update(id=id, label=True, tagging_status= True)
    Tagging.new_data_insert(scraped_id=id, tagger=getpass.getuser())
    return redirect('/')


@tagging_operations.route('/not_bulling/<int:id>')
def label_as_not_bully(id):
    Scraped.label_update(id=id, label=False, tagging_status= True)
    Tagging.new_data_insert(scraped_id=id, tagger=getpass.getuser())
    return redirect('/')

@tagging_operations.route('/delete/<int:id>')
def delete(id):
    #Zorbalık yok ama Tagging datasına(yani nihayi datasete) dahil edilmeyecek.
    Scraped.label_update(id=id, label=False, tagging_status= True)
    return redirect('/')