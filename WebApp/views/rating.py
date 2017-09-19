from flask import Blueprint, render_template

bp = Blueprint(__name__, __name__, template_folder = 'templates')

@bp.route('/rating')
def rating():
	return render_template('dashboard/rating.html')