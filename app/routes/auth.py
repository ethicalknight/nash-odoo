from flask import request, redirect, url_for, render_template, session, Blueprint, flash
from ..models import User
from ..db import SessionLocal

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/login', methods=['POST'])
def login():
    return render_template('login.html')
@auth_bp.route('/register')
def register():
    return render_template('register.html')
    if user:
        session['user_id'] = user.id
        return redirect(url_for('users.dashboard'))
    else:
        flash('Invalid credentials.')
        return redirect(url_for('auth.login_form'))
