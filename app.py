from flask import Flask
from flask_pymongo import PyMongo
from flask import jsonify,request

app= Flask(__name__)
app.secret.key == "secretkey"
app.config['MONGO_URI'] = "mongodb://localhost:27017/Students"

mongo =  PyMongo(app)
if __name__ == "__main__":
    app.run(debug="True")