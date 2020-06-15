import os
 
app_dir = os.path.abspath(os.path.dirname(__file__))

class BaseConfig:
    DEBUG = True
    POSTGRES_USER= 'hello'
    POSTGRES_PW = os.getenv('POSTGRE_SERVER_PW') 
    POSTGRES_DB= 'techconfdb'
    POSTGRES_SERVER= 'postgreserver-nd'
    POSTGRES_URL="postgresql://{user}%40{server}@{server}.postgres.database.azure.com:5432/{db}".format(user=POSTGRES_USER,server=POSTGRES_SERVER,db=POSTGRES_DB)
    DB_URL = 'postgresql://{user}:{pw}@{url}/{db}'.format(user=POSTGRES_USER,pw=POSTGRES_PW,url=POSTGRES_URL,db=POSTGRES_DB)
    SQLALCHEMY_DATABASE_URI = os.getenv('SQLALCHEMY_DATABASE_URI') or DB_URL
    CONFERENCE_ID = 1
    SECRET_KEY = 'LWd2tzlprdGHCIPHTd4tp5SBFgDszm' 
    SERVICE_BUS_CONNECTION_STRING = os.getenv('SERVICE_BUS_STRING') 
    SERVICE_BUS_QUEUE_NAME ='myndqueue'
    ADMIN_EMAIL_ADDRESS: 'info@techconf.com'
    SENDGRID_API_KEY = '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"'

class DevelopmentConfig(BaseConfig):
    DEBUG = True


class ProductionConfig(BaseConfig):
    DEBUG = False