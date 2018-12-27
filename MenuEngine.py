import DbClasses
from settings import sessionRepo,BaseEntitySet
from sqlalchemy import text, or_, and_
from sqlalchemy.exc import SQLAlchemyError


# This function is to fetch all the mneus based on the Menu Id (eg: hotels,resorts,adventure etc). ie menu details.
def get_menus(typeId):
    menuList = list()
    try:
        session = sessionRepo()
        db_result = session.query(DbClasses.menus_Repository,DbClasses.menuRoom_Repository,DbClasses.room_Repository).from_statement(text('''select room.id,app_room.room_id,menu.menu_id,
                                                                                menu.menu_name,menu.place_address,menu.city,menu.state,menu.country,
                                                                                app_room.room_name,room.cost,room.amenities,room.room_info 
                                                                                from tbl_app_menu_m as menu INNER JOIN tbl_menu_room_t as room
                                                                                ON menu.menu_id = room.menu_id
                                                                                INNER JOIN tbl_app_room_m as app_room
                                                                                ON app_room.room_id = room.room_id 
                                                                                where menu.type_id = :id''')).params(id=typeId).all()
        if db_result is None:
            response = BaseEntitySet(True, "Menu list not fetched from MenuRepository")
            return response

        for value in db_result:
            menu_json = {
                            "id" : value.menus_Repository.menu_id,
                            "name": value.menus_Repository.menu_name,
                            "address": value.menus_Repository.place_address,
                            "city": value.menus_Repository.city,
                            "state": value.menus_Repository.state,
                            "country": value.menus_Repository.country,
                            "type" : value.room_Repository.room_name,
                            "cost" : value.menuRoom_Repository.cost,
                            "amenities" : value.menuRoom_Repository.amenities,
                            "info" : value.menuRoom_Repository.room_info
                        }
            menuList.append(menu_json)
        BaseEntitySet(False, "Menu list fetched from MenuRepository")
        return menuList



    except SQLAlchemyError as error:
        print(error)
        BaseEntitySet(True, "Menu list not fetched from MenuRepository")


#This function is used for fetching the list from the db
def getMenuList(input):
    menuLists = list()
    menu_json = {
        "name": [],
    }

    session = sessionRepo()
    db_result_cities = session.query(DbClasses.menus_Repository).with_entities(DbClasses.menus_Repository.city).distinct(DbClasses.menus_Repository.city)\
        .filter(DbClasses.menus_Repository.city.ilike("%" + input + "%")).all()

    for value in db_result_cities:
        menu_json["name"].append(value.city)

    session = sessionRepo()
    db_result_menus = session.query(DbClasses.menus_Repository).with_entities(DbClasses.menus_Repository.menu_name).filter(DbClasses.menus_Repository.menu_name.ilike("%"+input+"%")).all()

    for value in db_result_menus:
        menu_json["name"].append(value.menu_name)
    menuLists = menu_json
    return menuLists


# This function is to obtain details of the selected Hotels or Reseorts. ie single menu details
def get_single_menu_details(menuId):
    menuList = list()
    try:
        session = sessionRepo()
        db_result = session.query(DbClasses.menus_Repository, DbClasses.menuRoom_Repository,
                           DbClasses.room_Repository).from_statement(text('''select room.id,app_room.room_id,menu.menu_id,
                                                                                    menu.menu_name,menu.place_address,menu.city,menu.state,menu.country,
                                                                                    app_room.room_name,room.cost,room.amenities,room.room_info 
                                                                                    from tbl_app_menu_m as menu INNER JOIN tbl_menu_room_t as room
                                                                                    ON menu.menu_id = room.menu_id
                                                                                    INNER JOIN tbl_app_room_m as app_room
                                                                                    ON app_room.room_id = room.room_id 
                                                                                    where menu.menu_id = :id ''')).params(id=menuId).all()
        if db_result is None:
            response = BaseEntitySet(True, "Selected Menu list is not fetched from MenuRepository")
            return response

        for value in db_result:
            menu_json = {
                "id": value.menus_Repository.menu_id,
                "name": value.menus_Repository.menu_name,
                "address": value.menus_Repository.place_address,
                "city": value.menus_Repository.city,
                "state": value.menus_Repository.state,
                "country": value.menus_Repository.country,
                "type": value.room_Repository.room_name,
                "cost": value.menuRoom_Repository.cost,
                "amenities": value.menuRoom_Repository.amenities,
                "info": value.menuRoom_Repository.room_info
            }
            menuList.append(menu_json)
        BaseEntitySet(False, "Selected Menu list fetched from MenuRepository")
        return menuList


    except SQLAlchemyError as error:
        print(error)
        BaseEntitySet(True, "Selected Menu list is not fetched from MenuRepository")


# This function is to return menus details which is entered in the search box by the user.
def get_searched_menu(input,typeId):
    search_result = []
    if input == '':
        exit()
    try:
        session = sessionRepo()
        db_result = session.query(DbClasses.menus_Repository).with_entities(DbClasses.menus_Repository.menu_id).filter( or_(DbClasses.menus_Repository.city.ilike("%" + input + "%"), DbClasses.menus_Repository.menu_name.ilike("%" + input + "%"))).filter(DbClasses.menus_Repository.type_id.ilike("%" + typeId + "%")).all()
        if db_result is None or db_result == '':
            response = BaseEntitySet(True, "Selected Menu ID  not fetched from MenuRepository")
            return response
        for id in range(len(db_result)):
            val = db_result[id]
            result = get_single_menu_details(val[0])
            search_result.append(result)
        if len(search_result) == 0:
            null_response = BaseEntitySet(True, "Selected Menu is not fetched from MenuRepository")
            return null_response
        return search_result
    except SQLAlchemyError as error:
        print(error)
        BaseEntitySet(True, "Selected Menu is not fetched from MenuRepository")
