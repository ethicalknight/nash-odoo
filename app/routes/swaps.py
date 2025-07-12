from flask import Blueprint, render_template, request
from ..models import SwapRequest
from ..db import SessionLocal

swap_routes = Blueprint("swap_routes", __name__)

@swap_routes.route("/requests")
def my_requests():
    db = SessionLocal()
    swaps = db.query(SwapRequest).all()
    db.close()
    return render_template("requests.html", swaps=swaps)
