from email.policy import default
import string
from urllib import request
import json

from sqlalchemy import null
from flask import Flask,jsonify,request,send_from_directory
from flask_sqlalchemy import SQLAlchemy
from py5paisa import FivePaisaClient
import threading
from pushnotifier import PushNotifier as pn
import time
import os
from flask_cors import CORS,cross_origin

from dotenv import load_dotenv
load_dotenv()
app = Flask(__name__,static_folder='./build',static_url_path='')
CORS(app)

app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
db = SQLAlchemy(app)


class Stockup(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    Exch = db.Column(db.String(2),default='N')
    ExchType = db.Column(db.String(2),default ='C')
    stock = db.Column(db.String,nullable=False)
    price = db.Column(db.Float, nullable=False)
    StrikePrice = db.Column(db.Float,default = 0)

class Stockdown(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    Exch = db.Column(db.String(2),default='N')
    ExchType = db.Column(db.String(2),default ='C')
    stock = db.Column(db.String,nullable=False)
    price = db.Column(db.Float, nullable=False)
    StrikePrice = db.Column(db.Float,default = 0)


db.create_all()