from flask import Blueprint, render_template, request, url_for

bp = Blueprint(__name__, __name__, template_folder = 'templates')

@bp.route('/login', methods=['POST', 'GET'])
def login():
	err = None
	if request.method == 'POST':
		if request.form['username']!='admin' or request.form['password']!='admin':
			err = 'Invalid Credentials. Please try again.'
		else:
			return redirect(url_for('/'))
	return render_template('login.html', error = err)