"""
@author: Vuong Quoc Viet
@version: 2.0
@since: Nov 23, 2017
"""

from __future__ import print_function
from flask import Blueprint, jsonify, request
from api.controls.helpers.user_getInformation import inforUser
from api.controls.handles.customtest import customtest as cu

api = Blueprint(__name__, __name__, template_folder='templates')


@api.route('/api/user/customtest', methods=['GET', 'POST'])
def customtest():
    userName = request.json['UserName']
    if request.method == 'POST':
        language = request.json['Lang']
        sourceCode = request.json['SourceCode']
        input = request.json['Input']

        print (sourceCode)
        hanlde = cu(userName, sourceCode, input, language)
        output = hanlde.getOutput()
        print (output)
        return jsonify({"Output": output})

    # data = inforUser(userName).getJson()
    # sourceCode = data['SourceCode']
    return jsonify({"SourceCode": "sourceCode"})
