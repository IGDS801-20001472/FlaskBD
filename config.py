import os
from sqlalchemy import create_engine
import urllib

class Config(object):
    SECRET_KEY = "ola ke ase"
    SESSION_COOKIE_SECURE = False

class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:@localhost/bdFlask801'
    SQLALCHEMY_TRACK_MODIFICATIONS = False