from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

db = SQLAlchemy()

def init_app(app:Flask):
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("DB_URI")
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False

    db.init_app(app)
    # Criar atributo
    app.db = db
    from app.models.call_record_model import CallRecord

    # db.create_all(app=app)
    # db.drop_all(app=app)