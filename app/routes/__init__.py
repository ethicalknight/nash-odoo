from .auth import auth_bp
from .public_feed import public_feed_bp
from .users import users_bp 
from .swaps import swap_routes
from ..db import SessionLocal



def register_routes(app):
    app.register_blueprint(auth_bp)
    app.register_blueprint(public_feed_bp)
    app.register_blueprint(swap_routes)
    app.register_blueprint(users_bp)
