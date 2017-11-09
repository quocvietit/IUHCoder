"""
@author: Vuong Quoc Viet
@version: 2.0
@since: Nov 9, 2017
"""

from flask import Flask
from api.user.api_user import api as user

api = Flask(__name__)
api.register_blueprint(user)

