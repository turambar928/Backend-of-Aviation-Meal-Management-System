from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from resources import db

class userModel(db.Model):
    __tablename__ = '用户数据'
    user_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    user_name: Mapped[str] = mapped_column(String(128), unique=True, nullable=False)
    user_password: Mapped[str] = mapped_column(String(128), nullable=False)

    def serialize(self):
        return{
            'id': self.user_id,
            'username': self.user_name
        }