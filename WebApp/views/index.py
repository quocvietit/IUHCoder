from flask import Blueprint, render_template, flash

bp = Blueprint(__name__, __name__, template_folder='templates')


@bp.route('/')
@bp.route('/index')
@bp.route('/home')
def show():
    return render_template('home/index.html')
