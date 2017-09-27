from flask import Blueprint, render_template, request, redirect, session, flash
from control.hanlde.Login import login as lg
import os

bp = Blueprint(__name__, __name__, template_folder='templates')


@bp.route('/login', methods=['POST', 'GET'])
def login():
    error = None
    if request.method == 'POST':
        form = lg(request.form)
        if (form.checkUser()):
            session['logged_in'] = True
            session['username'] = form.getUserName()
            flash("You were logged in")
            return redirect('/')
        else:
            error = 'Invalid user or password!'
    return render_template('user/login.html', error=error)
