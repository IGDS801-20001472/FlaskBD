import os
from sqlalchemy import create_engine
import urllib

class Config(object):
    SECRET_KEY = "ola ke ase"
    SESSION_COOKIE_SECURE = False

class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URL = 'mysql+pymysql://root:Gatitofeliz25@127.0.0.1:3307/bdFlask'
    SQLALCHEMY_TRACK_MODIFICATIONS = False