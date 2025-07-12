from flask import Flask
from .db import init_db
from .routes import register_routes

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'super-secret-key'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///skill_swap.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    init_db(app)
    register_routes(app)

    return app
