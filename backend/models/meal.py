from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Integer, String, Float

db = SQLAlchemy()

class mealModel(db.Model):
    __tablename__ = '航空餐食数据'

    # 定义列
    dish_id = db.Column(db.Integer, primary_key=True)
    dish_name = db.Column(db.String(100), nullable=False, unique=True)
    dish_remain = db.Column(db.Float, nullable=False)
    dish_number = db.Column(db.Integer, nullable=False)

    # 序列化方法
    def serialize(self):
        return {
            'dish_id': self.dish_id,
            'dish_name': self.dish_name,
            'dish_remain': self.dish_remain,
            'dish_number': self.dish_number
        }
