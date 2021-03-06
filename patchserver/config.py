import os

SECRET_KEY = os.urandom(32)

APP_DIR = os.path.dirname(os.path.realpath(__file__))

DEBUG = True
SQL_LOGGING = False

DATABASE_PATH = os.path.join(
    os.environ.get('DATABASE_DIR', APP_DIR), 'patch_server.db')

#SQLALCHEMY_DATABASE_URI = 'sqlite:////{}' .format(DATABASE_PATH)
SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI')
SQLALCHEMY_TRACK_MODIFICATIONS = False

RESET_API_TOKEN = os.path.exists(os.path.join(APP_DIR, 'reset_api_token'))
