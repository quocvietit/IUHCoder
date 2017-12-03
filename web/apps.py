from flask import Flask, session
from views.app_index import bp as index
from views.app_customtest import bp as customtest
from views.app_problems import bp as problems
from views.app_ratings import bp as rating
from views.app_contests import bp as contests
from views.app_user import bp as user
from views.app_info import bp as info
import os

app = Flask(__name__)
app.register_blueprint(index)
app.register_blueprint(customtest)
app.register_blueprint(problems)
app.register_blueprint(rating)
app.register_blueprint(contests)
app.register_blueprint(user)
app.register_blueprint(info)

if __name__ == '__main__':
    app.secret_key = os.urandom(12)
    app.run(debug=True, host=os.getenv('IP', '0.0.0.0'), port=int(os.getenv('PORT', 80)))
