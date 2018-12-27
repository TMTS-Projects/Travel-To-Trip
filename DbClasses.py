from settings import Base
from sqlalchemy import Column, Integer, String, Boolean, Date, ForeignKey


class type_Repository(Base):
    __tablename__ = 'tbl_app_type_m'
    type_id = Column("type_id",Integer, primary_key=True)
    type_name= Column("type_name",String)

class menus_Repository(Base):
    __tablename__ = 'tbl_app_menu_m'
    menu_id= Column("menu_id",Integer, primary_key=True)
    menu_name= Column("menu_name",String)
    place_address= Column("place_address", String)
    city = Column("city", String)
    state = Column("state", String)
    country = Column("country", String)
    pin_code = Column("pin_code", Integer)
    type_id = Column("type_id", Integer)

class user_Repository(Base):
    __tablename__ = 'tbl_app_user_m'
    user_id= Column("user_id",Integer, primary_key=True)
    initial= Column("initial",String)
    first_name= Column("first_name",String)
    last_name= Column("last_name",String)
    email_id= Column("email_id",String)
    mobile_number= Column("mobile_number",Integer)
    password= Column("password",String)
    is_guest= Column("is_guest",Boolean)


class room_Repository(Base):
    __tablename__ = 'tbl_app_room_m'
    room_id = Column("room_id", Integer, primary_key=True)
    room_name = Column("room_name", Integer)


class booking_Repository(Base):
    __tablename__ = 'tbl_booking_t'
    booking_id= Column("booking_id",Integer, primary_key=True)
    menu_id= Column("menu_id",Integer)
    room_id= Column("room_id",Integer)
    user_id= Column("user_id",Integer)
    check_in_date= Column("check_in_date",Date)
    check_out_date= Column("check_out_date",Date)
    no_of_persons= Column("no_of_persons",Integer)
    no_of_childs= Column("no_of_childs",Integer)
    no_of_rooms = Column("no_of_rooms", Integer)
    total_price = Column("total_price", Integer)

class menuRoom_Repository(Base):
    __tablename__ = 'tbl_menu_room_t'
    id= Column("id",Integer, primary_key=True)
    menu_id= Column("menu_id",Integer)
    room_id= Column("room_id",Integer)
    cost= Column("cost",Integer)
    amenities= Column("amenities",String)
    room_info= Column("room_info",String)
