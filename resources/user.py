import sqlite3
from flask_restful import Resource, reqparse # type: ignore
from models.user import UserModel




class UserRegister(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument("username", type = str, required = True, help = "username must be entered")
    parser.add_argument("password", type = str, required = True, help = "password must be entered")


    def post(self):
        data = UserRegister.parser.parse_args()

        if UserModel.find_by_username(data["username"]):
            return {"message": "a user with that username already exists"}, 400

        user = UserModel(**data)
        user.save_to_db()

        return {"message": "user successfully created"}, 201