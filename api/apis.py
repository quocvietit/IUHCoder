"""
@author: Vuong Quoc Viet
@version: 2.0
@since: Nov 9, 2017
"""

from flask import Flask
from apis.api_user import api as user
from apis.api_ratings import api as rating
from apis.api_customtest import api as customtest
import os

api = Flask(__name__)
api.register_blueprint(user)
api.register_blueprint(rating)
api.register_blueprint(customtest)

if __name__ == '__main__':
    api.secret_key = os.urandom(12)
    api.run(debug=True, host=os.getenv('IP', '0.0.0.0'), port=int(os.getenv('PORT', 3333)))

