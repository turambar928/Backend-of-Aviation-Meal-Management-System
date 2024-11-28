from routes import app
from flask import jsonify

@app.route('/')
def index():
    return "Welcome to the meal prediction API!"


@app.route('/api/meals/<meal_id>')
def get_meal(meal_id):
    meal = {'id': 2, 'name': 'sandwich', 'size': '0.5'}
    return jsonify(meal)

