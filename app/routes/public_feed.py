from flask import Blueprint, render_template
from ..models import User
from ..db import SessionLocal

public_feed_bp = Blueprint('public_feed', __name__)

@public_feed_bp.route('/')
def home():
    db = SessionLocal()
    users = db.query(User).filter_by(is_public=True).all()
    db.close()
    return render_template("index.html", users=users)
