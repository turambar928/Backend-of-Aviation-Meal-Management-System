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

    def put(self):
        try:
            # 获取请求的 JSON 数据
            request_json = request.json
            if not request_json:
                return {'error': 'Request body is empty'}, 400

            # 提取请求数据
            dish_id = request_json.get('dish_id')
            if dish_id is None:
                return {'error': 'dish_id is required'}, 400  # dish_id 必须提供

            dish_name = request_json.get('dish_name')
            dish_remain = request_json.get('dish_remain')
            dish_number = request_json.get('dish_number')

            # 创建 mealModel 实例
            meal_model = mealModel(
                dish_id=dish_id,
                dish_name=dish_name,
                dish_remain=dish_remain,
                dish_number=dish_number
            )

            # 调用服务层更新逻辑
            updated_meal = mealService().update_meal(meal_model)

            # 返回更新后的序列化数据
            return updated_meal.serialize()

        except Exception as error:
            return {'error': str(error)}, 400

    def post(self):
        try:
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
        except Exception as error:
            return {'error': str(error)}, 400


    def delete(self):
        try:
            # 从请求参数获取 dish_id
            dish_id = request.args.get('dish_id', type=int)
            if not dish_id:
                return {'error': 'dish_id is required'}, 400

            # 调用服务层删除逻辑
            result = mealService().delete_meal(dish_id)
            return result, 200
        except Exception as error:
            return {'error': str(error)}, 400

api.add_resource(MealResource, '/meals/<int:meal_id>')
api.add_resource(MealListResource, '/meals')



#xIuSLvgsq4*x  ALTER USER 'root'@'localhost' IDENTIFIED BY '623743';





