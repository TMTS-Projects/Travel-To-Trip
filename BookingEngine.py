import DbClasses
from settings import sessionRepo
from sqlalchemy.exc import SQLAlchemyError
from settings import BaseEntitySet


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
