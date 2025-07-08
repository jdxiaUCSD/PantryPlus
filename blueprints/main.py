from flask import Blueprint, request, render_template, flash, session, redirect, url_for
from flask_login import current_user
from app import db
from sqlalchemy import text
from models import Recipes, Goals

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
    goals = Goals.query.filter_by(user_id=current_user.get_id()).first()
    if goals:
        daily_protein = goals.daily_protein
        daily_carbohydrates = goals.daily_carbohydrates
        daily_fat = goals.daily_fat
        daily_fiber = goals.daily_fiber
        daily_calories = goals.daily_calories
        current_protein = 40
        current_carbohydrates = 130
        current_fat = 30
        current_fiber = 18
        current_calories = 2000

    else:
        print("Error fetching goals. Please create another account.")
        return redirect(url_for('auth.login'))
    return render_template('/main/dashboard.html', 
        recipes=recipes, 
        username = current_user.username,
        daily_protein = daily_protein,
        daily_carbohydrates = daily_carbohydrates,
        daily_fat = daily_fat,
        daily_fiber = daily_fiber,
        daily_calories = daily_calories,
        current_protein = current_protein,
        current_carbohydrates = current_carbohydrates,
        current_fat = current_fat,
        current_fiber = current_fiber,
        current_calories = current_calories
        )


@main_bp.route('/delete_all')
def delete_all():
    try:
        Recipes.query.delete()
        db.session.commit()
    except:
        db.session.rollback()
    return redirect(url_for('main.dashboard'))
