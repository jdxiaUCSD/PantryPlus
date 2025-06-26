from app import db
from flask_login import UserMixin


class User(db.Model, UserMixin):
    __tablename__ = "users"

    uid = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String, nullable = False)
    password = db.Column(db.String, nullable = False)
    email = db.Column(db.String, nullable = False)
    #backref = user adds a user attribute to every recipe/goal object
    #cascade = when you save/update user, applies to recipes. if a recipe becomes disconnected from its user
    #delet it
    recipes = db.relationship('Recipes', backref='user', lazy=True, cascade='all, delete-orphan')
    nutritional_goals = db.relationship('Goals', backref='user', lazy=True, cascade='all, delete-orphan')

    def __repr__(self):
        return f'<User: {self.username}'

    def get_id(self):
        return str(self.uid)



class Goals(db.Model):
    __tablename__ = 'fitness_goals'

    id = db.Column(db.Integer, primary_key = True)
    daily_protein = db.Column(db.Integer)
    daily_carbohydrates = db.Column(db.Integer)
    daily_fat = db.Column(db.Integer)
    daily_fiber = db.Column(db.Integer)
    daily_calories = db.Column(db.Integer)
    allergy = db.Column(db.Text)

    user_id = db.Column(db.Integer, db.ForeignKey('users.uid'), nullable = False)
    
    def __repr__(self):
        return f'<NutritionalGoal for User {self.user_id}>'
    
class Recipes(db.Model):
    __tablename__ = 'recipes'

    id = db.Column(db.Integer, primary_key = True, nullable = False)
    ingredients = db.Column(db.Text, nullable = False)
    instructions = db.Column(db.Text, nullable = False)
    cooking_time = db.Column(db.Integer)
    prep_time = db.Column(db.Integer)
    servings = db.Column(db.Integer)

    protein_amount = db.Column(db.Integer)
    carb_amount = db.Column(db.Integer)
    fiber_amount = db.Column(db.Integer)
    fat_amount = db.Column(db.Integer)
    calorie_amount = db.Column(db.Integer)

    user_id = db.Column(db.Integer, db.ForeignKey('users.uid'), nullable = False)


