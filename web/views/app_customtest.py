from flask import Blueprint, render_template, request, session, redirect
import requests

bp = Blueprint(__name__, __name__, template_folder='templates')


@bp.route('/customtest', methods=['POST', 'GET'])
def customtest():
    if request.method == 'GET' and not session.get('username'):
        return redirect('login')

    data = {
        "Lang": None,
        "SourceCode": None,
        "Input": None,
        "Output": None
    }

    userName = session.get('username')

    if request.method == 'GET':

        reponse = requests.get("http://localhost:3333/api/user/customtest/" + userName).json()

        if "Lang" in reponse:
            data['Lang'] = reponse['Lang']
            data['SourceCode'] = reponse['SourceCode']

    if request.method == 'POST':
        postData = {
            "Lang": request.form['language'],
            "SourceCode": request.form['sourcecode'],
            "Input": request.form['input']
        }

        reponse = requests.post("http://localhost:3333/api/user/customtest/" + userName, json=postData).json()

        data['Lang'] = postData['Lang']
        data['SourceCode'] = postData['SourceCode']
        data['Input'] = postData['Input']
        data['Output'] = reponse['Output']

    return render_template("customtest/customtest.html", data = data)
