"""
@author: Vuong Quoc Viet
@version: 2.0
@since: Nov 1, 2017
"""
from __future__ import print_function
from flask import Blueprint
from control.helper.InfoUser import infoUser as info

api = Blueprint(__name__, __name__, template_folder='templates')

@api.route('/api/user/<username>/profile')
def user(username):
    return info().getInfoUser(username)







