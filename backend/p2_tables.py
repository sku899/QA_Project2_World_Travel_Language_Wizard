from flask_sqlalchemy import SQLAlchemy
from flask import Flask

appdb = Flask(__name__)
appdb.config['SECRET_KEY'] = 'YOUR_SECRET_KEY'
username='me'
password = 'qwerty123'
ocalhost = 'localhost:3306'
database = 'flaskdb'

#app.config["SQLALCHEMY_DATABASE_URI"] = f"mysql+pymysql://{username}:{password}@{localhost}/{database}"
appdb.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://me:qwerty123@127.0.0.1:3306/flaskdb2"
appdb.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 
db = SQLAlchemy(appdb)




class Events(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    country_name = db.Column(db.String(10), nullable=False)
    words = db.Column(db.String(30), nullable=False)

db.drop_all()
db.create_all()