from flask import Flask
from webApp.views.Index import bp as index_bp
from webApp.views.Customtest import bp as customtest_bp
from webApp.views.Problems import bp as problems_bp
from webApp.views.rating import bp as rating_bp
from webApp.views.contests import bp as contests_bp
from webApp.views.Login import bp as login_bp
from webApp.views.About import bp as about_bp
from webApp.views.Register import bp as register_bp
from webApp.views.Logout import bp as logout_bp

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


