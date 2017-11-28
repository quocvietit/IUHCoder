from web.apps import app
from api.apis.api_user import api as test
from flask import session
import os

if __name__ == '__main__':
    # app.run(debug=True)

    app.secret_key = os.urandom(12)
    app.run(debug=True, host=os.getenv('IP', '0.0.0.0'), port=int(os.getenv('PORT', 80)))
    session['logged_in'] = True
