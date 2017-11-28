from __future__ import print_function

from flask import Blueprint, render_template, request, session, flash
import requests

bp = Blueprint(__name__, __name__, template_folder='templates')


@bp.route('/register/', methods=['POST', 'GET'])
def register():
    try:
        error = None
        if request.method == 'POST':

            data = {
                "username": request.form['username'],
                "password": request.form['password']
            }

            reponse = requests.post("http://localhost:3333/api/user/register", json=data).json();

            if (reponse['status'] == 'True'):
                flash("Thanks for registering!")
                session['logged_in'] = True
                session['username'] = request.form['username']
                return render_template('home/index.html')
            else:
                error = 'User exits!'

        return render_template('user/register.html', error=error)
    except Exception as e:
        return str(e)
