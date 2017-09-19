from __future__ import print_function
from flask import Blueprint, render_template, request, redirect, url_for, session, flash
from controlPanels.entities.RegistrationForm import registrationForm
from controlPanels.entities.User import user

bp = Blueprint(__name__, __name__, template_folder='templates')


def getDataForm(form):
    return registrationForm(form['userName'], form['password'], form['confirmPassword'])


@bp.route('/register/', methods=['POST', 'GET'])
def register():
    try:
        error = None
        if request.method == 'POST':

            form = getDataForm(request.form)

            # check password
            if (form.checkPassword()):
                newUser = user(form.getUserName(), form.getPassword())

                if (newUser.addUser()):
                    flash("Thanks for registering!")
                    session['logged_in'] = True
                    session['username'] = newUser.getUserName()

                    return render_template('home/index.html')
                else:
                    error = 'User exits!'
            else:
                error = 'Password not match!'

        return render_template('user/register.html', error=error)
    except Exception as e:
        return str(e)
