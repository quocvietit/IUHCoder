from flask import Blueprint, render_template, request, url_for, redirect, session, flash

bp = Blueprint(__name__, __name__, template_folder='templates')


@bp.route('/login', methods=['POST', 'GET'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['userName'] != 'admin':
            error = 'Invalid Username'
        elif request.form['password'] != 'admin':
            error = 'Invalid Password'
        else:
            session['logged_in'] = True
            session['username'] = request.form['userName']
            flash("You were logged in")
            return redirect('/')
    return render_template('user/login.html', error=error)
