from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from flask import session
import smtplib,os
from smtplib import SMTPException, SMTPAuthenticationError

engine = create_engine('mysql+pymysql://sa:TMTSserver@31@3.86.39.214:9000/travel_to_trip', echo=True)
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


def send_mail(to,subject,body):
    TO = to
    SUBJECT = subject
    TEXT = body
    gmail_sender = ''
    gmail_passwd = ''
    try:
        server = smtplib.SMTP('smtp.gmail.com',587)
        server.ehlo()
        server.starttls()
        server.login(gmail_sender, gmail_passwd)

        BODY = '\r\n'.join(['To: %s' % TO,
                            'From: %s' % gmail_sender,
                            'Subject: %s' % SUBJECT,
                            '', TEXT])


        server.sendmail(gmail_sender, [TO], BODY)
        result = BaseEntitySet(False, "e-mail sent successfully")
        server.quit()
        return result
    except SMTPAuthenticationError as e_Error:
        print(e_Error)
        BaseEntitySet(True, "The username and/or password you entered for e-mail is incorrect")

    except SMTPException as e_excpn:
        print(e_excpn)
        BaseEntitySet(True, "Error occurred while sending e-mail")


