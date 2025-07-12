from flask import Flask
from .db import init_db


def create_app():
    app = Flask(__name__)
    # Add your config here
    from .routes import auth_bp, public_feed_bp, users_bp, swaps_bp  
    app.register_blueprint(auth_bp)
    app.register_blueprint(public_feed_bp)
    app.register_blueprint(users_bp)
    app.register_blueprint(swaps_bp)

    with app.app_context():
        init_db()  # create tables on first run

    return app
