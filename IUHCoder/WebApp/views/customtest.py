from flask import Blueprint, render_template, request
from ControlPanels.controler.Customtest import customtes as ct

bp = Blueprint(__name__, __name__, template_folder='templates')


@bp.route('/customtest', methods=['POST', 'GET'])
def show():
    if request.method == 'POST':
        if request.form.get('customtest'):
            codeText = request.form.get('codetext')
            inputText = request.form.get('inputtext')
            ct(codeText, inputText)

    return render_template("customtest.html")
