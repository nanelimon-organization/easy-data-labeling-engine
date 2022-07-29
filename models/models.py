from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()


# Kazınmış Veri Tablosu
class Scraped(db.Model):
    __tablename__ = 'scraped'
    id = db.Column('id', db.Integer, primary_key=True)
    text = db.Column('text', db.String(300))
    label = db.Column('label', db.String(100))
    tagging_status = db.Column('tagging_status', db.Boolean, default=False)

    def label_update(id, label, tagging_status):
        updating = Scraped.query.where(Scraped.id == id).first()
        updating.label = label
        updating.tagging_status = tagging_status
        db.session.add(updating)
        db.session.commit()


# Etiketleme Tablosu
class Tagging(db.Model):
    __tablename__ = 'tagging'
    id = db.Column('id', db.Integer, primary_key=True, autoincrement=True, nullable=False)
    scraped_id = db.Column('scraped_id', db.Integer)
    tagger = db.Column('tagger', db.String(100))
    tagged_date = db.Column('tagged_date', db.DateTime, default=datetime.now())

    def new_data_insert(scraped_id, tagger):
        inserting = Tagging(
            scraped_id=scraped_id,
            tagger=tagger
        )
        db.session.add(inserting)
        db.session.commit()
