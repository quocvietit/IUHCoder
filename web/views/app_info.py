from flask import Blueprint, render_template

bp = Blueprint(__name__, __name__, template_folder='templates')


@bp.route('/about')
def about():
    return render_template('info/about.html')


@bp.route('/api')
def api():
    return render_template('info/api.html')
