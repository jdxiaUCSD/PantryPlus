from flask import Blueprint, request, render_template, flash, session, redirect, url_for
from flask_login import current_user
from models import Recipes, User
from app import db

gen_bp = Blueprint('recipegen', __name__, url_prefix = '/generate')

@gen_bp.route('/')
def index():
    return render_template('/generate/generate.html')

@gen_bp.route('/processing', methods = ['POST'])
def process():
    title = request.form.get('title')
    ingredients = request.form.get('ingredients')
    instructions = request.form.get('instructions')
    cooking_time = request.form.get('cooking_time')
    prep_time = request.form.get('prep_time')
    servings = request.form.get('servings')
    protein_amount = request.form.get('protein_amount')
    carb_amount = request.form.get('carb_amount')
    fiber_amount = request.form.get('fiber_amount')
    fat_amount = request.form.get('fat_amount')
    calorie_amount = request.form.get('calorie_amount')

    user_id = current_user.get_id()
    
    recipe = Recipes(
        title = title,
        ingredients = ingredients,
        instructions = instructions,
        cooking_time = cooking_time,
        prep_time = prep_time,
        servings = servings,
        protein_amount = protein_amount,
        carb_amount = carb_amount,
        fiber_amount = fiber_amount,
        fat_amount = fat_amount,
        calorie_amount = calorie_amount,
        user_id = user_id
    )
    
    db.session.add(recipe)

    db.session.commit()
    
    return redirect(url_for('main.dashboard'))