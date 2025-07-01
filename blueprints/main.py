from flask import Blueprint, request, render_template, flash, session, redirect, url_for
from flask_login import current_user
from app import db
from sqlalchemy import text
from models import Recipes

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def index():
    # if (current_user.is_authenticated):
    #     return redirect(url_for('main.dashboard'))
    # else:
    return redirect(url_for('auth.login'))

@main_bp.route('/dashboard')
def dashboard():
    recipes = Recipes.query.all()
    
    return render_template('/main/dashboard.html', recipes=recipes, username = current_user.username)


@main_bp.route('/delete_all')
def delete_all():
    try:
        Recipes.query.delete()
        db.session.commit()
    except:
        db.session.rollback()
    return redirect(url_for('main.dashboard'))