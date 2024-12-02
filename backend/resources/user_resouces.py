from flask import request
from flask_restful import Resource

from resources import api
from services.user_service import UserService


class LoginResource(Resource):
    def post(self):
        try:
            request_json = request.json()
            if request_json:
                username = request_json.get('username',None)
                password = request_json.get('password',None)

                user_model = UserService().login(username, password)
                if user_model:
                    user_json = user_model.serialize()

                    return user_json
                else:
                    return {'message':'Username or password error'}, 401

            else:
                return {'message':'please provide username and password as json'}, 400

        except Exception as error:
            return {'message':str(error)}, 400


api.add_resource(LoginResource, '/login')
