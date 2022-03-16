from email.policy import default
import string
from urllib import request
import json

from sqlalchemy import null
from flask import Flask,jsonify,request,send_from_directory
from flask_sqlalchemy import SQLAlchemy
from py5paisa import FivePaisaClient
import threading
from notify_run import Notify
import time
import os
from flask_cors import CORS,cross_origin

from dotenv import load_dotenv
load_dotenv()
app = Flask(__name__,static_folder='./build',static_url_path='')
CORS(app)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///stockup.sqlite"
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



exit_event = threading.Event()
# def eventhandlerstop():
#     exit_event.set()


def eventhandlerstart():
    exit_event.clear()

notify = Notify()

@app.route('/')
def serve():
    return send_from_directory(app.static_folder,'index.html')

# stockup backend
def stockup_serializer(stockup):
    return{
        "id":stockup.id,
        "stock":stockup.stock,
        "price":stockup.price
    }
@app.route('/showstockup', methods=['GET', 'POST'])
def showstockup():
    allstock= Stockup.query.all()
    datatosend = jsonify([*map(stockup_serializer,allstock)])
    return datatosend

@app.route('/createstockup', methods=['GET', 'POST'])
def createstockup():
    data = json.loads(request.data)
    addstock = Stockup(stock=data['stock'].upper(),price=data['price'])
    db.session.add(addstock)
    db.session.commit()
    return{"202":"stockup added successfully"}

@app.route('/updatestockup', methods=['GET', 'POST'])
def updatestockup():
    data = json.loads(request.data)
    stockupdate = Stockup.query.filter_by(id=data['id']).first()
    stockupdate.stock = data['stock'].upper()
    stockupdate.price = data['price']
    db.session.add(stockupdate)
    db.session.commit()
    return{"203":"stockup edited successfully"}


@app.route('/deletestockup/<int:id>', methods=['GET', 'POST'])
def deletestockup(id):
    id = int(id)
    Stockup.query.filter_by(id=id).delete()
    db.session.commit()
    return{"204":"stockup deleted"}

# stockdown backend
def stockdown_serializer(stockdown):
    return{
        "id":stockdown.id,
        "stock":stockdown.stock,
        "price":stockdown.price
    }
@app.route('/showstockdown', methods=['GET', 'POST'])
def showstockdown():
    allstock= Stockdown.query.all()
    datatosend = jsonify([*map(stockdown_serializer,allstock)])
    return datatosend

@app.route('/createstockdown', methods=['GET', 'POST'])
def createstockdown():
    data = json.loads(request.data)
    addstock = Stockdown(stock=data['stock'].upper(),price=data['price'])
    db.session.add(addstock)
    db.session.commit()
    return{"302":"stockdown added successfully"}

@app.route('/updatestockdown', methods=['GET', 'POST'])
def updatestockdown():
    data = json.loads(request.data)
    stockdowndate = Stockdown.query.filter_by(id=data['id']).first()
    stockdowndate.stock = data['stock'].upper()
    stockdowndate.price = data['price']
    db.session.add(stockdowndate)
    db.session.commit()
    return{"303":"stockdown edited successfully"}


@app.route('/deletestockdown/<int:id>', methods=['GET', 'POST'])
def deletestockdown(id):
    id = int(id)
    Stockdown.query.filter_by(id=id).delete()
    db.session.commit()
    return{"304":"stockdown deleted"}


# This is market fecthing backend
@app.route('/startfeed')
def startfeed():
    return{'406':'streaming started'}

# print(type(os.getenv("app_name")))
# print(type(os.getenv("app_source")))
# print(type(os.getenv("user_id")))
# print(type(os.getenv("password")))
# print(type(os.getenv("user_key")))
# print(type(os.getenv("encryption_key")))
# print(type(os.getenv("email")))
# print(type(os.getenv("passwd")))
# print(type(os.getenv("dob")))

cred={
    "APP_NAME":os.getenv("app_name"),
    "APP_SOURCE":os.getenv("app_source"),
    "USER_ID":os.getenv("user_id"),
    "PASSWORD":os.getenv("password"),
    "USER_KEY":os.getenv("user_key"),
    "ENCRYPTION_KEY":os.getenv("encryption_key")
    }

client = FivePaisaClient(email=os.getenv("email"), passwd=os.getenv("passwd"), dob=os.getenv("dob"),cred=cred)
client.login()

# def get_price():
#     stockup = Stockup.query.all()
#     stockdown = stockdown.query.all()
#     for stock in stockup :
# @app.route('/test')
# def test():
    
#     stockup = Stockup.query.all()
#     for stock in stockup :
#         print(type(stockup))
#     return{'eh':'df'}

def stock_for_market_serializer(stock):
    return {
        "Exch":stock.Exch,
        "ExchType" : stock.ExchType,
        "Symbol" : stock.stock,
        "StrikePrice": stock.StrikePrice
    }
th = []
def streaming():
    
    exit_event.clear()

    def checkprice ():
        while True :
            if exit_event.is_set():
                    # print("closing stream")
                    break
            stockup = Stockup.query.all()
            # for loop for stock price increase threashould
        
            if len(stockup) !=0:
                req_market_list_stockup = [*map(stock_for_market_serializer,stockup)]
                data_dict_stockup = client.fetch_market_feed(req_market_list_stockup)
                data_stockup = data_dict_stockup['Data']
                # print(data_stockup)

                for i in range(len(data_stockup)):
                    for stock in stockup:
                        if stock.stock == data_stockup[i]['Symbol']:
                            if float(data_stockup[i]['LastRate'])>stock.price:
                                notify.send(f"{stock.stock},{float(data_stockup[i]['LastRate'])}")
                                Stockup.query.filter_by(stock=stock.stock,price=stock.price).delete()
                                db.session.commit()
            else :
                # print('list empty')
                pass
    
            stockdown = Stockdown.query.all()
            # for loop for stock price decrease threashould
            if len(stockdown)!=0 :
                req_market_list_stockdown = [*map(stock_for_market_serializer,stockdown)]
                data_dict_stockdown = client.fetch_market_feed(req_market_list_stockdown)
                data_stockdown = data_dict_stockdown['Data']
                # print(data_stockdown)
                for i in range(len(data_stockdown)):
                    for stock in stockdown:
                        if stock.stock == data_stockdown[i]['Symbol']:
                            if float(data_stockdown[i]['LastRate'])<stock.price:
                                notify.send(f"{stock.stock},{float(data_stockup[i]['LastRate'])}")
                                Stockdown.query.filter_by(stock=stock.stock,price=stock.price).delete()
                                db.session.commit()
            else :
                # print('list empty2')
                pass
            time.sleep(2)
    if len(th)==0:
        # print('iff....................')
        t1 = threading.Thread(target=checkprice,
                                name=checkprice)  
                                    
        t1.start()
      
        th.append(t1)
    else :
        pass
def eventhandler():
    exit_event.set()
    th.pop()
# class runonce :
#     run_once = null
# r = runonce()
# r.run_once = 0
@app.route('/startstreaming')
def startstream():
    
        streaming()
        return{"22":"streaming"}
   

#NOTE : Symbol has to be in the same format as specified in the example below.


@app.route('/stopstreaming')
def stopstreaming():
    eventhandler()
    return{"23":"streaming stopped"}
@app.route('/registernotify')
def registernotify():
    val = notify.register()
  
    return jsonify(str(val))
@app.route('/send')
def send():
    notify.send('hello')
    return str('djfs')
if __name__ == '__main__':
    app.run()