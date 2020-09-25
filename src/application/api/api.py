from flask import Blueprint, request, url_for, redirect, session, jsonify
from flask import current_app as app

# blueprint configuration
api_bp = Blueprint('api_bp', __name__)

@api_bp.route("/auth", methods=["GET"])
def get_auth():
    """
    Returns a view to verify that the user wants to authorize the requested
    application's request for the supplied scopes.
    """
    return "GET /auth"

@api_bp.route("/auth", methods=["POST"])
def post_auth():
    """
     Verifies that the authorization code is valid, has not yet been used,
     and that it was issued for the matching client_id and redirect_uri.
    """
    return jsonify({"response": "POST /auth"})

@api_bp.route("/token", methods=["GET"])
def get_token():
    """
     If a resource server needs to verify that an access token is valid, it
     MUST make a GET request to the token endpoint containing an HTTP
     Authorization header with the Bearer Token according to [RFC6750].

     Note: the request to the endpoint will not contain any user-identifying
     information, so the resource server (e.g. Micropub endpoint) will need
     to know via out-of-band methods which token endpoint is in use.
    """
    return "GET /token"

@api_bp.route("/token", methods=["POST"])
def post_token():
    """
     The token endpoint needs to verify that the authorization code is valid,
     and that it was issued for the matching client_id and redirect_uri, and
     contains at least one scope. If the authorization code was issued with no
     scope, the token endpoint MUST NOT issue an access token, as empty scopes
     are invalid per Section 3.3 of OAuth 2.0 [RFC6749].
    """
    return jsonify({"response": "POST /token"})

