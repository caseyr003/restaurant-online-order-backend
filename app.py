import json
from flask import Flask, request, jsonify
from flask_cors import cross_origin

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database import Base, User, Order

# declare constants
HOST = '0.0.0.0'
PORT = 5000

# connect to database
engine = create_engine('sqlite:///restaurant-online-order.db')
Base.metadata.bind = engine
# create database session
DBSession = sessionmaker(bind=engine)
session = DBSession()

# initialize flask application
app = Flask(__name__)


# api endpoint for orders
@app.route('/orders', methods=['GET', 'POST'])
@cross_origin()
def orders():
    if request.method == 'POST':
        # get data from post request
        data = request.get_json()
        if data.keys() >= {'customer', 'cost', 'items'}:
            # create new order
            new_order = Order(user_id=data['customer']['id'],
                              cost=data['cost'],
                              lettuce=data['items']['lettuce'],
                              cheese=data['items']['cheese'],
                              bacon=data['items']['bacon'],
                              meat=data['items']['meat'],)
            session.add(new_order)
            session.commit()
            # return success status and new order
            return jsonify(status=201, order=new_order.serialize)
        else:
            # return error status
            return jsonify(status=400)
    else:
        # get all orders for user
        orders = session.query(Order).filter_by(user_id=1).all()
        return jsonify(status=200, orders=[i.serialize for i in orders])


# api endpoint for initial items
@app.route('/items')
@cross_origin()
def items():
        # get initial items
        return jsonify(
            items={
                'lettuce':1, 
                'cheese':1, 
                'bacon':0, 
                'meat':1
            }
        )


if __name__ == '__main__':
    app.run(host=HOST,
            debug=True,
            port=PORT)
