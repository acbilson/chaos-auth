from os import path
import toml

basedir = path.abspath(path.dirname(__file__))
config = toml.load(path.join(basedir, "config.toml"))

class Config:

    """Set Flask configuration variables"""
    FLASK_ENV = config["FLASK_ENV"]

    SESSION_SECRET = config["SESSION_SECRET"]
    SECRET_KEY = config["SECRET_KEY"]
    CLIENT_ID = config["oauth"]["github"]["client_id"]
    CLIENT_SECRET = config["oauth"]["github"]["client_secret"]

    LOCAL = config['LOCAL']
    REMOTE = config['REMOTE']
    BASE_SITE = config['BASE_SITE']

    # cache configuration
    CACHE_TYPE = config["CACHE_TYPE"]
    CACHE_DIR = config["CACHE_DIR"]
    CACHE_DEFAULT_TIMEOUT = config["CACHE_DEFAULT_TIMEOUT"]

    # TODO: remove when no longer dependent
    # user-specific configuration
    NAME = "Alex Bilson"
    PHOTO_URL = "https://alexbilson.dev/selfie"
    EMAIL = "acbilson@gmail.com"
    ADDRESS = ""
    LOCALITY = "Evanston"
    REGION = "IL"
    COUNTRY = "USA"
