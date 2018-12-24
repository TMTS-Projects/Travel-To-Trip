from flask import Flask, redirect, url_for, request, render_template,session
import json
import MenuEngine,TravellorsEngine,BookingEngine
from settings import create_session

app = Flask(__name__)
app.secret_key = "123"

@app.route('/')
def home():
    return render_template('keypress.html')

@app.route('/menus', methods=["POST"])
def get_menu():
    MenuIdJson = request.get_json()
    create_session(key="menuId",value=MenuIdJson["typeId"])
    result = MenuEngine.get_menus(typeId=session["menuId"])
    response = json.dumps(result)
    return response

@app.route('/pressedMenus', methods=["POST"])
def get_menu_list():
    MenuIdJson = request.get_json()
    result = MenuEngine.getMenuList(input=MenuIdJson["text"])
    response = json.dumps(result)
    return response



@app.route('/singleMenu', methods=["POST"])
def get_menu_details():
    SingleMenuIdJson = request.get_json()
    result = MenuEngine.get_single_menu_details(menuId=SingleMenuIdJson["menuId"])
    response = json.dumps(result)
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
