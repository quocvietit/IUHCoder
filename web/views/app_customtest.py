from flask import Blueprint, render_template, request, session, redirect
from control.hanlde.Customtest import customtest as cu

bp = Blueprint(__name__, __name__, template_folder='templates')


@bp.route('/customtest', methods=['POST', 'GET'])
def customtest():
    if request.method == 'POST':
        hanlde = cu(request.form, session.get('username'))
        session['outputCustemtest'] = hanlde.getOutput()
        session['sourceCode'] = request.form['sourceCode']
        session['input'] = request.form['input']
    if request.method == 'GET' and not session.get('logged_in'):
        return redirect('login')
    return render_template("customtest/customtest.html")
