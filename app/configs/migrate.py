from flask import Flask
from flask_migrate import Migrate

# 1 - Primeira forma
# mg = Migrate()

def init_app(app:Flask):
    # Usando a primeira forma
    # mg.init_app(app=app, db=app.db)

    # Segunda forma
    Migrate(app=app, db=app.db, compare_type=True)