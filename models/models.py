from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


# Etiketleme Tablosu
class Tagging(db.Model):
    __tablename__ = 'tagging'
    id = db.Column('id', db.Integer, primary_key=True, autoincrement=True)
    label = db.Column('label', db.Boolean, default=True)
    text = db.Column('text', db.String(8))
    tagger = db.Column('tagger', db.DateTime)
    date = db.Column('date', db.DateTime)
