from flask import Blueprint, request, url_for, redirect, session
from flask import current_app as app

# blueprint configuration
core_bp = Blueprint('core_bp', __name__)

@core_bp.route("/")
def index():
    return "Alive!"
