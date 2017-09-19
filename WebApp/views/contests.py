from flask import Blueprint, render_template, request

bp = Blueprint(__name__, __name__, template_folder='templates')

@bp.route('/contests')
def show():
    return render_template('dashboard/contests.html')
