"""
@author: Vuong Quoc Viet
@version: 2.0
@since: Nov 1, 2017
"""

from flask import Blueprint, render_template, request, redirect, session, flash
import requests
import socket

bp = Blueprint(__name__, __name__, template_folder='templates')


@bp.route('/login', methods=['POST', 'GET'])
def login():
    error = None
    if request.method == 'POST':

        data = {
            "UserName": request.form['username'],
            "Password": request.form['password']
        }
        #print 'http://' + socket.gethostbyname(socket.gethostname()) + '/api/user/login'
        reponse = requests.post("http://localhost/api/user/login", json=data).json()
        if(reponse['status'] == 'True'):
            session['logged_in'] = True
            session['username'] = request.form['username']
            flash("You were logged in")
            return redirect('/')
        else:
            error = 'Invalid username or password!'

    return render_template('user/login.html', error=error)
