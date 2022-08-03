from flask import make_response, jsonify

from app.api.v1 import blueprint_v1
from app.api.v1.services.auth import public_auth_client


@blueprint_v1.route("/auth/token", methods=["GET", "POST"])
def get_token():
    return make_response(jsonify({
        "access_token": public_auth_client['access_token'],
        "expires_in": public_auth_client['expires_in']
    }), 200)
