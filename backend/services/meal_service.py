from models.meal import mealModel
from resources import db
from sqlalchemy import Select


class mealService:
    def get_meal_by_id(self, meal_id: int):
        return db.session.get(mealModel, meal_id)

    def get_all_meals(self):
        query = Select(mealModel).order_by(mealModel.dish_id)
        return db.session.scalars(query).all()

    def create_meal(self, meal: mealModel):
        db.session.add(meal)
        db.session.commit()

        return meal