from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from flask import session

engine = create_engine('mysql+pymysql://sa:TMTSserver@31@3.84.25.27:9000/travel_to_trip', echo=True)
Base = declarative_base()

def sessionRepo():
    Session = sessionmaker()
    Session.configure(bind=engine)
    session=Session()
    return session


def create_session(key,value):
    Session = session[key, value]
    return Session
