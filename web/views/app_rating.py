"""
@author: Vuong Quoc Viet
@version: 1.1
@since: Sep 27, 2017
"""

from flask import Blueprint, render_template
from control.hanlde.Rating import Rating

bp = Blueprint(__name__, __name__, template_folder='templates')


@bp.route('/rating')
def rating():
    return render_template('dashboard/rating.html', ratings=Rating().get_list())
