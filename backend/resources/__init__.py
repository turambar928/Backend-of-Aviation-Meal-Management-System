from flask_restful import Api
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:623743@localhost:3306/demo'
db = SQLAlchemy(app)

from resources import meal_resources


