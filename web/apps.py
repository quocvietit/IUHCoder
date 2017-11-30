from flask import Flask, session
from web.views.app_index import bp as index_bp
from web.views.app_customtest import bp as customtest_bp
from web.views.app_problems import bp as problems_bp
from web.views.app_ratings import bp as rating_bp
from web.views.app_contests import bp as contests_bp
from web.views.app_user import bp as user
from web.views.app_info import bp as info
import os

app = Flask(__name__)
app.register_blueprint(index_bp)
app.register_blueprint(customtest_bp)
app.register_blueprint(problems_bp)
app.register_blueprint(rating_bp)
app.register_blueprint(contests_bp)
app.register_blueprint(user)
app.register_blueprint(info)

if __name__ == '__main__':
    app.secret_key = os.urandom(12)
    app.run(debug=True, host=os.getenv('IP', '0.0.0.0'), port=int(os.getenv('PORT', 80)))