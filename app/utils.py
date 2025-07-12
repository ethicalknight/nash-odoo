from flask import session
from .models import User

def get_current_user():
    from .db import db
    user_id = session.get("user_id")
    if user_id:
        return db.session.get(User, user_id)
    return None
