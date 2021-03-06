from flask import Flask, redirect, url_for, request, render_template, session
import json
import MenuEngine, TravellorsEngine, BookingEngine
from settings import create_session

app = Flask(__name__)
app.secret_key = "123"


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/menus', methods=["POST"])
def get_menu():
    MenuIdJson = request.get_json()
    create_session(key="menuId", value=MenuIdJson["typeId"])
    response = json.dumps({"isFailure":True,"message":"Value Set"}, default=lambda o: o.__dict__)
    return response


@app.route('/SearchedMenus', methods=["POST"])
def searched_menu():
    SearchJson = request.get_json()
    create_session(key="checkin", value=SearchJson["checkin"])
    create_session(key="checkout", value=SearchJson["checkout"])
    create_session(key="rooms", value=SearchJson["rooms"])
    create_session(key="input", value=SearchJson["input"])
    return "/SearchMark"


#Searching for resorts and hotels
@app.route('/SearchMark')
def search_mark():
    result = MenuEngine.get_searched_menu(input=session["input"], typeId=session["menuId"])
    #create_session(key="city", value=result.menuList[0][0]['city'])
    response = json.dumps(result, default=lambda o: o.__dict__)
    if session["checkin"] != "NaN-aN-aN" and session["checkout"] != "NaN-aN-aN":
        return render_template("filterPage.html", details=result,city=session["city"],checkin=session["checkin"],checkout=session["checkout"])
    elif session["checkin"] == "NaN-aN-aN" and session["checkout"] == "NaN-aN-aN":
        return render_template("filterPage.html", details=result, city=" Chikmagalur", checkin='', checkout='')


@app.route('/pressedMenus', methods=["POST"])
def get_menu_list():
    MenuIdJson = request.get_json()
    result = MenuEngine.getMenuList(typeId=session["menuId"], input=MenuIdJson["text"])
    response = json.dumps(result, default=lambda o: o.__dict__)
    return response


@app.route('/singleMenu', methods=["POST"])
def get_menu_details():
    SingleMenuIdJson = request.get_json()
    result = MenuEngine.get_single_menu_details(menuId=SingleMenuIdJson["menuId"])
    # create_session(key="menuName", value=result["name"])
    # create_session(key="location", value=result["city"])
    # create_session(key="cost", value=result["cost"])
    response = json.dumps(result, default=lambda o: o.__dict__)
    return response


@app.route('/filteredMenus', methods=['POST'])
def get_filter_menu_list():
    FilterJson = request.get_json()
    result = MenuEngine.filter_menu_list(typeId=session["menuId"],city="Chikmagalur",fromValue=FilterJson["min"],toValue=FilterJson["max"])
    return render_template("priceFilterPage.html", details=result, city="Chikmagalur", checkin=session["checkin"], checkout=session["checkout"])



@app.route('/confirmedMenu', methods=["POST"])
def confirmed_menu():
    ConfirmJson = request.get_json()
    create_session(key="confirm", value=ConfirmJson["id"])
    return "/confirmedDetails"



@app.route('/confirmedDetails')
def get_confirmed_menu_list():
    result = MenuEngine.get_single_menu_details(menuId=session["confirm"])
    return render_template("finalbooking.html",details=result)



@app.route('/travellors', methods=["POST"])
def travellors():
    jsonData = request.get_json()
    response = TravellorsEngine.insert_traveller_details(jsonData)
    return response

@app.route('/bookings', methods=["POST"])
def bookings():
    jsonData = request.get_json()
    response = BookingEngine.booking_Repository_details(jsonData)
    return response


if __name__ == '__main__':
    app.run(debug=True)
