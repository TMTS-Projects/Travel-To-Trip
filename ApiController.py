from flask import Flask, redirect, url_for, request, render_template,session
import os,json
import DbClasses
import TravellorsEngine
import BookingEngine
from settings import create_session



app = Flask(__name__)



@app.route('/')
def LogIn():
    return render_template('')


@app.route('/menus', methods=["POST"])
def get_json():
    jsonData = request.get_json()
    create_session(key="menuId",value=jsonData["menuId"])

    response= json.dumps( )
    return response


@app.route('/singleMenu', methods=["POST"])
def get_json():
    jsonData = request.get_json()

    response = json.dumps()
    return response

@app.route('/travellors', methods=["POST"])   #Reddy this is your routing
def travellors():
    jsonData = request.get_json()
    response=TravellorsEngine.insert_traveller_details(jsonData)
    return response

@app.route('/bookings', methods=["POST"])
def bookings():
    jsonData = request.get_json()
    response = BookingEngine.booking_Repository_details(jsonData)
    return response





if __name__ == '__main__':
    app.run(debug=True)
