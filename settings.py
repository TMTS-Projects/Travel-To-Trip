from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from flask import session

engine = create_engine('mysql+pymysql://sa:TMTSserver@31@3.82.153.226:9000/travel_to_trip', echo=True)
Base = declarative_base()

def sessionRepo():
    Session = sessionmaker()
    Session.configure(bind=engine)
    session=Session()
    return session


def create_session(key, value):
    session[key] = value


def BaseEntitySet(flag,message):
    jsonData = dict()
    jsonData["Isfailure"] = flag
    jsonData["message"] = message
    if flag == True:
        print(jsonData["message"])
    return jsonData["message"]


