from flask import Blueprint, request, render_template, flash, session, redirect, url_for
from flask_login import current_user
from models import Recipes, User
from app import db

gen_bp = Blueprint('recipegen', __name__, url_prefix = '/generate')

# Initialize optimized model loader (singleton pattern)

@gen_bp.route('/')
def index():
    return render_template('/generate/generate.html')

@gen_bp.route('/processing')
def process():
    return "processing?"

@gen_bp.route('/create_temp')
def create_temp():
    title = 'Black Pepper Steak'
    ingredients = "450 g (1 lb) thin steak sliced thinly, against the grain (I use sirloin), 2 tsp freshly ground black pepper, tsp salt, tbsp sunflower oil"
    instructions = "Toss the steak slices with 1 tsp of the black pepper and the salt. 450 g (1 lb) thin steak, 2 tsp freshly ground black pepper, 1/4 tsp salt. Heat 3 tbsp of the sunflower oil and the sesame oil in a wok (or large frying pan) over a high heat until hot, then add the steak."
    cooking_time = 15
    prep_time = 15
    servings = 4
    protein_amount = 120
    carb_amount = 70
    fiber_amount = 10
    fat_amount = 110
    calorie_amount = 1600
    difficulty = 'Easy'

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
        user_id = user_id,
        difficulty = difficulty
    )

    db.session.add(recipe)

    db.session.commit()
    
    return redirect(url_for('main.dashboard'))

@gen_bp.route('/generate', methods = ['POST'])
def generate():
    """Generate recipes using optimized AI models"""
    query = request.form.get('query')
    
    if not query:
        flash('Please enter a recipe query', 'error')
        return redirect(url_for('recipegen.index'))
    
    # try:
    #     # Use optimized batch inference for recipe generation
    #     results = model_loader.batch_inference([query], RECOMMENDED_MODELS['fast'])
        
    #     # For now, return the query (you can expand this with actual recipe generation)
    #     # TODO: Implement actual recipe generation logic using the model results
    #     flash(f'Generated recipe for: {query}', 'success')
        
    # except Exception as e:
    #     flash(f'Error generating recipe: {str(e)}', 'error')
    
    return redirect(url_for('recipegen.index'))
