from sqlalchemy import Select

from models.user import userModel
from resources import db


class UserService:
    def login(self, username: str, password: str):
        query = Select(userModel).where(userModel.username == username)
        user_model = db.session.scalars(query).first()
        if user_model and user_model.password == password:
            return user_model
        else:
            return None