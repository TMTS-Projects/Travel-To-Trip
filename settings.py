from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('mysql+pymysql://sa:TMTSserver@31@34.205.144.198:9000/travel_to_trip', echo=True)
Base = declarative_base()

def sessionRepo():
    Session = sessionmaker()
    Session.configure(bind=engine)
    session=Session()
    return session


