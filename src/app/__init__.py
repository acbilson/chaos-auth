import logging
from flask import Flask, Response
from flask_cors import CORS

from app.auth import auth_bp
from app import config


def create_app(config=config.BaseConfig):
    """Initialize the core application"""
    app = Flask(__name__, instance_relative_config=False)
    cors = CORS(app)
    app.config.from_object(config)

    # required to encrypt session
    app.secret_key = app.config["FLASK_SECRET_KEY"]

    register_extensions(app)

    with app.app_context():

        # register blueprints
        app.register_blueprint(auth_bp)

        print(app.config)

        @app.route("/healthcheck", methods=["GET"])
        def health():
            return Response(status=200)

        return app


def register_extensions(app):
    """Register extensions with the Flask application."""
    pass
