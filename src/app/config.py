from os import environ


class BaseConfig(object):
    """Set Flask configuration variables"""

    FLASK_HOST = "0.0.0.0"
    FLASK_PORT = 80
    FLASK_ENV = environ.get("FLASK_ENV")
    SITE = environ.get("SITE")

    ADMIN_USER = environ.get("ADMIN_USER")
    ADMIN_PASSWORD = environ.get("ADMIN_PASSWORD")

    FLASK_SECRET_KEY = environ.get("FLASK_SECRET_KEY")
    SESSION_SECRET = environ.get("SESSION_SECRET")


class TestConfig(object):
    """Set Flask test configuration variables"""

    FLASK_HOST = "0.0.0.0"
    FLASK_PORT = 80
    FLASK_ENV = "development"
    SITE = "http://localhost/"

    FLASK_SECRET_KEY = "my secret test key"
    SESSION_SECRET = "my secret test session"
