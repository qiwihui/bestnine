import os

class BaseConfig(object):
    SECRET_KEY = os.environ['SECRET_KEY']
    DEBUG = os.environ['DEBUG']
