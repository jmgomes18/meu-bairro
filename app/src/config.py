import os

from dotenv import load_dotenv

load_dotenv()

postgres_local_base = os.environ.get("DATABASE_URL", "sqlite://")


class Config(object):
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL", "sqlite://")
    SECRET_KEY = os.getenv("API_SECRET_KEY", "my_precious_secret_key")
    AUTH_DOMAIN = os.getenv("AUTH_DOMAIN")
    CLIENT_ID = os.getenv("CLIENT_ID")
    AUTH_SECRET = os.getenv("AUTH_SECRET")
    DEBUG = False


class DevelopmentConfig(Config):
    SQLALCHEMY_DATABASE_URI = postgres_local_base
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DEBUG = True


class TestingConfig(Config):
    SQLALCHEMY_DATABASE_URI = postgres_local_base
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    PRESERVE_CONTEXT_ON_EXCEPTION = False
    TESTING = True
    DEBUG = True


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = postgres_local_base
    DEBUG = False


config_by_name = dict(dev=DevelopmentConfig, test=TestingConfig, prod=ProductionConfig)

key = Config.SECRET_KEY
