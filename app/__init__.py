from flask import Flask
from app.configs import database, migrate
from app import routes

def create_app():
    app = Flask(__name__)
    app.config["JSON_SORT_KEYS"] = False
    # Primeiro a database
    database.init_app(app)
    # Depois a migrate
    migrate.init_app(app)
    routes.init_app(app)
    return app