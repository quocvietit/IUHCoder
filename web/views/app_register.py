from __future__ import print_function

from flask import Blueprint, render_template, request, session, flash

from control.hanlde.Register import register as rs

bp = Blueprint(__name__, __name__, template_folder='templates')


@bp.route('/register/', methods=['POST', 'GET'])
def register():
    try:
        error = None
        if request.method == 'POST':

            form = rs(request.form)

            # check password
            if (form.checkPassword()):
                a = form.registerUser()
                print(a)
                if (a):
                    flash("Thanks for registering!")
                    session['logged_in'] = True
                    session['username'] = form.getUserName()
                    return render_template('home/index.html')
                else:
                    error = 'User exits!'
            else:
                error = 'Password not match!'

        return render_template('apis/register.html', error=error)
    except Exception as e:
        return str(e)
