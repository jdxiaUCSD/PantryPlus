from flask import Blueprint, request, render_template, flash, session, redirect, url_for
from models import User, Goals
from app import db, bcrypt

register_bp = Blueprint('register', __name__, url_prefix = '/register')

@register_bp.route('/')
def register():
    return render_template('/register/step1.html')

@register_bp.route('/step1', methods = ['POST', 'GET'])
def step1():
    if (request.method == 'POST'):
        username = request.form.get('Username')
        password = request.form.get('Password')
        hashed_password = bcrypt.generate_password_hash(password)

        email = request.form.get('Email')
        #add some edge case stuff here--maybe a confirm password/make sure that username/emails aren't already taken
        #if forms are not filled out, redirect back to step1

        session['registration_data'] = {
            'username' : username,
            'password' : hashed_password,
            'email' : email
        }
        return render_template('/register/step2.html')

    return render_template('register/step1.html')

@register_bp.route('/step2', methods = ['POST', 'GET'])
def step2():
    if (request.method == 'POST'):
        daily_calories = request.form.get('daily_calories')
        daily_carbohydrates = request.form.get('daily_carbohydrates')
        daily_fat = request.form.get('daily_fat')
        daily_fiber = request.form.get('daily_fiber')
        daily_protein = request.form.get('daily_protein')

        #check that numbers are valid (>0, maybe make sure that numbers look right <20000 calories)
        #if forms are not filled out, redirect back to step1

        session['registration_data']['fitness_goals'] = {
            'daily_calories' : daily_calories,
            'daily_carbohydrates' : daily_carbohydrates,
            'daily_fat' : daily_fat,
            'daily_fiber' : daily_fiber,
            'daily_protein' : daily_protein
        }

        session.modified = True

        return render_template('/register/step3.html')
    # Are we able to submit post requests through url?? idk man
    return render_template('register/step1.html')


@register_bp.route('/step3', methods = ['POST', 'GET'])
def step3():
    if (request.method == 'POST'):
        allergy = request.form.get('allergies')
        session['registration_data'].update({'allergy' : allergy})
        #check that numbers are valid (>0, maybe make sure that numbers look right <20000 calories)
        #if forms are not filled out, redirect back to step1
        session.modified = True
        return render_template('register/confirm.html')
    return render_template('register/step1.html')

@register_bp.route('/confirm', methods = ['POST', 'GET'])
def confirm():
    if (request.method == 'POST'):
        user = User(
            username = session['registration_data']['username'], 
            password = session['registration_data']['password'],
            email = session['registration_data']['email'],
        )
        db.session.add(user)
        db.session.flush()

        fitness_goals = session['registration_data']['fitness_goals']
        goal = Goals(
            daily_protein = session['registration_data']['fitness_goals']['daily_protein'],
            daily_carbohydrates = session['registration_data']['fitness_goals']['daily_carbohydrates'],
            daily_fat = session['registration_data']['fitness_goals']['daily_fat'],
            daily_fiber = session['registration_data']['fitness_goals']['daily_fiber'],
            daily_calories = session['registration_data']['fitness_goals']['daily_calories'],
            allergy = session['registration_data']['allergy'],
            user_id = user.uid
        )

        db.session.add(goal)

        db.session.commit()

        session.pop('registration_data', None)

        flash('Registration Successful! Please log in :)')

        # flash('confirm if statement hit')
        return redirect(url_for('auth.login'))
    
    # flash('confirm if statement NOT hit')
    return redirect(url_for('auth.login'))


