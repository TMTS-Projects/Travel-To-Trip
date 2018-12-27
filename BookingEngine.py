import datetime

import DbClasses
from settings import sessionRepo
from sqlalchemy.exc import SQLAlchemyError
from settings import BaseEntitySet
from MenuEngine import get_single_menu_details

def booking_Repository_details(json_data):

    try:
        session = sessionRepo()
        booking=DbClasses.booking_Repository()
        booking.check_in_date=json_data["check_in_date"]
        booking.check_out_date=json_data["check_out_date"]
        booking.no_of_persons=json_data["no_of_persons"]
        booking.no_of_childs=json_data["no_of_childs"]
        booking.no_of_rooms=json_data["no_of_rooms"]
        booking.total_price=json_data["total_price"]
        session.add(booking)
        session.commit()
        response = BaseEntitySet(False, "Data inserted to the booking repository")
        return response

    except SQLAlchemyError as error:
        print(error)
        response = BaseEntitySet(True, "Data not inserted to the booking repository")
        return response


# This function returns total cost of the booking.
def calculate_rent(selectedId,menuName,cost,checkIn,checkOut,rooms):
    menuDetails = get_single_menu_details(menuId=selectedId)
    if checkIn == '' and checkOut == '':
        response = BaseEntitySet(True, "Please provide CheckIn and CheckOut Date")
        return response
    try:
        d1 = datetime.date(int(checkIn[0:4]), int(checkIn[5:7]), int(checkIn[8:10]))
        d2 = datetime.date(int(checkOut[0:4]), int(checkOut[5:7]), int(checkOut[8:10]))
        delta = d2 - d1
        day = str(delta)
        nights = int(day[0:2])
        TotalCost = menuDetails[0]['cost'] * nights * rooms

        TotalCost_Json = {
                            "total" : TotalCost,
                            "calculation" : str(menuDetails[0]['cost']) + "*" + str(nights) + "*" + str(rooms)
                            }
        return TotalCost_Json
    except ValueError as error:
        print(error)
        response = BaseEntitySet(True, "Please provide CheckIn and CheckOut Date")
        return response


