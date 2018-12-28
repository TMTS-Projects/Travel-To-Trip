from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from flask import session
import smtplib,os,sys,logging
from smtplib import SMTPException, SMTPAuthenticationError
from sqlalchemy.exc import SQLAlchemyError

try:
    engine = create_engine('mysql+pymysql://sa:TMTSserver@31@54.173.57.41:9000/travel_to_trip', echo=True)
    Base = declarative_base()
except SQLAlchemyError as error:
    print(error)
    exc_type, exc_obj, exc_tb = sys.exc_info()
    fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
    print(fname, exc_tb.tb_lineno)




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




def store_error_log(message):
    str_msg = str(message)
    exc_type, exc_obj, exc_tb = sys.exc_info()
    fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
    exp = str_msg+ "   -    " + fname + "   -   " + str(exc_tb.tb_lineno)
    filename = 'errorlog.log'
    if not os.path.exists(filename):
        file = open(filename, 'w+')
        file.close()

    logging.basicConfig(filename=filename, level=logging.DEBUG, format='%(asctime)s %(message)s')
    logging.error(exp)








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
        store_error_log(e_excpn)
        BaseEntitySet(True, "Error occurred while sending e-mail")


