import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    # ...
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        "postgresql://postgres:postgres@localhost:54320/postgres"
    SQLALCHEMY_TRACK_MODIFICATIONS = False