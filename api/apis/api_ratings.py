"""
@author: Vuong Quoc Viet
@version: 2.0
@since: Nov 18, 2017
"""

from __future__ import print_function
from flask import Blueprint, jsonify
from api.controls.helpers.rating_getList import rating

api = Blueprint(__name__, __name__, template_folder='templates')


@api.route('/api/user/ratings', methods=['GET'])
def getListRating():
    listRating = rating().getListRatingByJsonFormat()
    return jsonify(listRating)
