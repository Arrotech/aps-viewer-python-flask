from flask import Blueprint
"""Group related views."""

blueprint_v1 = Blueprint('blueprint_v1', __name__, template_folder='../../../templates', static_folder='../../../static')

from app.api.v1.views import auth, models # noqa
from app.api.v1.services import auth, oss, md # noqa