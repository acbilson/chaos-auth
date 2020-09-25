from flask import Flask
from flask_dance.contrib.github import make_github_blueprint, github
from flask_caching import Cache
import sys
import logging
from logging import StreamHandler

# globally accessible libraries
cache = None

def create_app():
    """Initialize the core application"""
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object('config.Config')
    app = config_log(app)

    # required to encrypt session
    app.secret_key = app.config['SECRET_KEY']

    # initialize plugins
    cache = Cache(app)

    with app.app_context():
        # import parts of the app
        from .core import core
        from .api import api

        # register blueprints
        app.register_blueprint(core.core_bp)
        app.register_blueprint(api.api_bp)

        # registers github blueprint from flask-dance
        github_blueprint = make_github_blueprint(
            client_id=app.config['CLIENT_ID'],
            client_secret=app.config['CLIENT_SECRET'],
        )
        app.register_blueprint(github_blueprint, url_prefix="/login")

        app.logger.info('initialized auth app')
        return app

def config_log(app):
    """ Configure logging for this application """
    stream_handler = StreamHandler(sys.stdout)

    if app.debug:
        app.logger.setLevel(logging.DEBUG)
    else:
        app.logger.setLevel(logging.INFO)

    app.logger.addHandler(stream_handler)
    return app

