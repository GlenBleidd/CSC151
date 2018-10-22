import os
basedir = os.path.abspath(os.path.dirname(__file__))
DB_NAME = "StudentDB"
DB_HOST = "localhost"
DB_USERNAME = "postgres"
DB_PASSWORD = "regards"
DB_CONN_STRING = "postgresql://%s:%s@%s:5432/%s" % (DB_USERNAME,DB_PASSWORD,DB_HOST,DB_NAME)
SECRET_KEY="sawa"