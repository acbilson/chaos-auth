from flask import Flask
from flask_dance.contrib.github import make_github_blueprint, github
from flask_caching import Cache

# globally accessible libraries
cache = None

def create_app():
    """Initialize the core application"""
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object('config.Config')

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

        return app
