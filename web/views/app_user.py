from flask import Blueprint, render_template, request, redirect, session, flash
import requests

bp = Blueprint(__name__, __name__, template_folder='templates')


@bp.route('/register/', methods=['POST', 'GET'])
def register():
    try:
        error = None
        if request.method == 'POST':

            data = {
                "UserName": request.form['username'],
                "Password": request.form['password']
            }

            reponse = requests.post("http://localhost:3333/api/user/register", json=data).json()

            if (reponse['Status'] == 'True'):
                flash("Thanks for registering!")
                session['username'] = request.form['username']
                return render_template('home/index.html')
            else:
                error = 'User exits!'

        return render_template('user/register.html', error=error)
    except Exception as e:
        return str(e)


@bp.route('/login', methods=['POST', 'GET'])
def login():
    error = None
    if request.method == 'POST':

        data = {
            "UserName": request.form['username'],
            "Password": request.form['password']
        }

        reponse = requests.post("http://localhost:3333/api/user/login", json=data).json()

        if (reponse["Status"] == 'True'):
            session['username'] = request.form['username']
            flash("You were logged in")
            return redirect('/')
        else:
            error = 'Invalid username or password!'

    return render_template('user/login.html', error=error)


@bp.route('/logout')
def logout():
    session.clear()
    flash("You were logged out")
    return redirect('/')
