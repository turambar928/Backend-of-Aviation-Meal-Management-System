from models.meal import mealModel
from resources import db
from sqlalchemy import Select


class mealService:
    def get_meal_by_id(self, meal_id: int):
        return db.session.get(mealModel, meal_id)

    def get_all_meals(self):
        query = Select(mealModel).order_by(mealModel.dish_id)
        return db.session.scalars(query).all()

    def get_meal_by_name(self, meal_name: str):
        query = Select(mealModel).where(mealModel.dish_name == meal_name)
        return db.session.scalars(query).all()

    def create_meal(self, meal: mealModel):
        exist_meal = self.get_meal_by_name(meal.dish_name)
        if exist_meal:
            raise Exception("Meal already exists with name")
        db.session.add(meal)
        db.session.commit()

        return meal

    def update_meal(self, meal: mealModel):
        exist_meal = self.get_meal_by_id(meal.dish_id)
        if not exist_meal:
            raise Exception("Meal does not exist")

        if meal.dish_name:
            exist_meal.dish_name = meal.dish_name
        if meal.dish_number:
            exist_meal.dish_number = meal.dish_number
        if meal.dish_remain:
            exist_meal.dish_remain = meal.dish_remain

        db.session.commit()
        return exist_meal

    def delete_meal(self, meal: mealModel):
        #检查是否存在
        exist_meal = self.get_meal_by_id(meal.dish_id)
        if not exist_meal:
            raise Exception("Meal does not exist")
        #删除
        db.session.delete(exist_meal)
        db.session.commit()
        return {"message": f"Meal with dish_id {meal.dish_id} has been deleted"}
