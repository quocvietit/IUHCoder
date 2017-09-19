from flask import Blueprint, render_template, request, url_for, redirect, session, flash
from Login import login
bp = Blueprint(__name__, __name__, template_folder='templates')


@bp.route('/logout')
def logout():
    session.pop('logged_in', None)
    flash("You were logged out")
    return redirect('/')
