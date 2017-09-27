from flask import Flask
from web.views.app_index import bp as index_bp
from web.views.app_customtest import bp as customtest_bp
from web.views.app_problems import bp as problems_bp
from web.views.app_rating import bp as rating_bp
from web.views.app_contests import bp as contests_bp
from web.views.app_login import bp as login_bp
from web.views.app_about import bp as about_bp
from web.views.app_register import bp as register_bp
from web.views.app_logout import bp as logout_bp

app = Flask(__name__)
app.register_blueprint(index_bp)
app.register_blueprint(customtest_bp)
app.register_blueprint(problems_bp)
app.register_blueprint(rating_bp)
app.register_blueprint(contests_bp)
app.register_blueprint(login_bp)
app.register_blueprint(logout_bp)
app.register_blueprint(about_bp)
app.register_blueprint(register_bp)


