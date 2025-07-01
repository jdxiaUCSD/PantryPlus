from flask import Blueprint, request, render_template, flash, session, redirect, url_for, get_flashed_messages
from flask_login import login_user
from models import User
from app import db, bcrypt
import logging, traceback

auth_bp = Blueprint('auth', __name__, url_prefix = '/auth')

@auth_bp.route('/', methods = ['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username').strip()
        password = request.form.get('password')
        if not username or not password:
            flash('Please enter username and password')
        try:
            user = User.query.filter(User.username == username).first()
            if user and bcrypt.check_password_hash(user.password, password):
                login_user(user)
                return redirect(url_for("main.dashboard"))
            else:
                flash('Incorrect Login credentials')
        except Exception as e:
            logging.error(f"An error occurred: {e}")
            traceback.print_exc()
            flash('An exception has occured. Please try again.')
    return render_template('/auth/login.html')
#Maybe do Google Log in integration down the line?

@auth_bp.route('/log_out')
def log_out():
    session.pop('_flashes', None)
    flash('Logout Successful')
    return redirect(url_for('auth.login'))
