from db import db
from flask import Flask
from flask_restful import Api # type: ignore
from flask_jwt import JWT # type: ignore
from security import authenticate, identity
from resources.user import UserRegister
from resources.item import Item, ItemList
from resources.store import Store, StoreList

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:////Users/zack.lindberg/Documents/section7/code/mydata.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.secret_key = "zack"
api = Api(app)
jwt = JWT(app, authenticate, identity)

api.add_resource(Store, "/store/<string:name>")
api.add_resource(Item, "/item/<string:name>")
api.add_resource(ItemList, "/items")
api.add_resource(StoreList, "/stores")
api.add_resource(UserRegister, "/register")

@app.before_first_request
def create_tables():
    db.create_all()

if __name__ == "__main__":
    db.init_app(app)
    app.run(port=5000, debug=True)