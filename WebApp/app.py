from flask import Flask
from WebApp.views.Index import bp as index_bp
from WebApp.views.Customtest import bp as customtest_bp
from WebApp.views.Problems import bp as problems_bp
from WebApp.views.rating import bp as rating_bp
from WebApp.views.contests import bp as contests_bp
from WebApp.views.Login import bp as login_bp
from WebApp.views.about import bp as about_bp
from WebApp.views.Register import bp as register_bp
from WebApp.views.Logout import bp as logout_bp

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


