import DbClasses
from settings import sessionRepo,create_session

def insert_traveller_details(json_data):

    session=sessionRepo()
    user= DbClasses.user_Repository()
    user.first_name=json_data["first_name"]
    user.last_name = json_data["last_name "]
    user.mobile_number=json_data["mobile_number"]
    user.initial=json_data["initial"]
    user.is_guest=json_data["is_guest"]
    user.password=json_data["password"]
    session.add(user)
    session.commit()
    return True




