"""
@author: Vuong Quoc Viet
@version: 2.0
@since: Nov 1, 2017
"""

from __future__ import print_function
from flask import Blueprint, request, jsonify
from controls.helpers.user_getInformation import inforUser
from controls.handles.user_resgister import register as rs
from controls.handles.user_login import login as lg

api = Blueprint(__name__, __name__, template_folder='templates')


@api.route('/api/user/<string:username>', methods=['GET'])
@api.route('/api/user/<string:username>/profile', methods=['GET'])
def getInformationUser(username):
    data = inforUser(username).getJson()
    if 'username' in request.args:
        return data["UserName"]
    return data


@api.route('/api/user/register', methods=['POST'])
def registerUser():
    userName = request.json['UserName']
    password = request.json['Password']
    return jsonify({"Status": str(rs(userName, password).registerUser())})


@api.route('/api/user/login', methods=['POST'])
def loginUser():
    userName = request.json['UserName']
    password = request.json['Password']
    return jsonify({"Status": str(lg(userName, password).checkUser())})
