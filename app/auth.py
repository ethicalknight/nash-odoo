from flask import Blueprint, request, redirect, url_for, session, render_template
from werkzeug.security import generate_password_hash, check_password_hash
from .db import SessionLocal
from .models import User

auth_bp = Blueprint('auth', __name__)

@auth_bp.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        password = request.form["password"]
        location = request.form["location"]
        is_public = request.form.get("is_public") == "true"
        hashed_pw = generate_password_hash(password)

        user = User(name=name, email=email, password=hashed_pw, location=location, is_public=is_public)
        db_session = SessionLocal()
        db_session.add(user)
        db_session.commit()
        db_session.close()

        return redirect(url_for("auth.login"))
    return render_template("register.html")


@auth_bp.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]

        user = User.query.filter_by(email=email).first()
        if user and check_password_hash(user.password, password):
            session["user_id"] = user.id
            return redirect(url_for("index"))
        return "❌ Invalid credentials", 401
    return render_template("login.html")


@auth_bp.route("/logout")
def logout():
    session.pop("user_id", None)
    return redirect(url_for("auth.login"))
