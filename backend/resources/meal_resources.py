from flask import request
from flask_restful import Resource

from models import meal
from models.meal import mealModel
from resources import api
from services.meal_service import mealService


class MealResource(Resource):
    def get(self, meal_id: int):
        meal = mealService().get_meal_by_id(meal_id)
        if meal:
            return meal.serialize()



    def post(self):
        pass

    def put(self, meal_id: int):
        pass

class MealListResource(Resource):
    def get(self):
        meal_list = mealService().get_all_meals()
        return [meal.serialize() for meal in meal_list]

    def post(self):
        request_json = request.json
        if request_json:
            dish_id = request_json.get('dish_id', None)
            dish_name = request_json.get('dish_name', None)
            dish_remain = request_json.get('dish_remain', None)
            dish_number = request_json.get('dish_number', None)

            meal_model = mealModel(dish_id = dish_id, dish_name = dish_name, dish_remain = dish_remain, dish_number = dish_number)
            mealService().create_meal(meal_model)

            return meal_model.serialize()
        else:
            return {'error': 'Request body is empty'}, 400

api.add_resource(MealResource, '/meals/<int:meal_id>')
api.add_resource(MealListResource, '/meals')


#xIuSLvgsq4*x  ALTER USER 'root'@'localhost' IDENTIFIED BY '623743';





