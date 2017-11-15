from web.apps import app
from api.apis.api_user import api as test
import os

if __name__ == '__main__':
    # app.run(debug=True)
    app.secret_key = os.urandom(12)
    app.register_blueprint(test)
    app.run(debug=True, host=os.getenv('IP', '0.0.0.0'), port=int(os.getenv('PORT', 80)))
