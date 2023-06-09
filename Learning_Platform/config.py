from os import environ

SECRET_KEY = environ.get("SECRET_KEY")
DEBUG = bool(environ.get("DEBUG"))
ALLOWED_HOSTS = environ.get("ALLOWED_HOSTS").split()
WEB_PORT = environ.get("WEB_PORT")

POSTGRES_DB = environ.get("POSTGRES_DB")
POSTGRES_USER = environ.get("POSTGRES_USER")
POSTGRES_PASSWORD = environ.get("POSTGRES_PASSWORD")
POSTGRES_HOST = environ.get("POSTGRES_HOST")
POSTGRES_PORT = environ.get("POSTGRES_PORT")
