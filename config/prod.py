"""

AUTOR: Juanjo

FECHA DE CREACIÓN: 08/07/2019

"""
from .default import *
import os


SECRET_KEY = os.getenv('secret_key_env')

APP_ENV = APP_ENV_PRODUCTION

SQLALCHEMY_DATABASE_URI = os.getenv('SQLALCHEMY_DATABASE_URI')
