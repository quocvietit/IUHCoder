from flask import Blueprint, render_template, request

bp = Blueprint(__name__, __name__, template_folder = 'templates')

@bp.route('/customtest', methods=['POST', 'GET'])
def show():
	if request.method == 'POST':
		if request.form.get('customtest'):
			text = request.form.get('notetext')
			return text
	return render_template('customtest.html')