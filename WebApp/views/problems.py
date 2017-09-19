from flask import Blueprint, render_template

bp = Blueprint(__name__, __name__, template_folder = 'templates')

@bp.route('/problems')
def problems():
	return render_template('dashboard/problems.html', problems = problems)