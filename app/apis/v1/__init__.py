from flask import Blueprint
from flask_cors import CORS

bp = Blueprint('api_v1', __name__)
CORS(bp)

from app.apis.v1 import resources