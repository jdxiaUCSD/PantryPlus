from flask import Blueprint, request, render_template, flash, session, redirect, url_for
from flask_login import current_user
main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def index():
    # if (current_user.is_authenticated):
    #     return redirect(url_for('main.dashboard'))
    # else:
    return redirect(url_for('auth.login'))

#include routes for dashboard and recipes

@main_bp.route('/dashboard')
def dashboard():
    return render_template("/main/dashboard.html", user = current_user)