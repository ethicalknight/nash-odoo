from flask import Blueprint, render_template
users_bp = Blueprint("users", __name__)

@users_bp.route("/profile")
def profile():
    return render_template("profile.html")  # Or whatever your profile file is named
