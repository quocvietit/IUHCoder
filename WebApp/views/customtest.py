from flask import Blueprint, render_template, request
from ControlPanels.controler.Customtest import customtes as ct

bp = Blueprint(__name__, __name__, template_folder='templates')
output = ""

@bp.route('/customtest', methods=['POST', 'GET'])
def show():
    if request.method == 'POST':
        if request.form.get('customtest'):
            codeText = request.form.get('mycode')
            inputText = request.form.get('inputtext')
            output = ct(codeText, inputText)
    return render_template("customtest.html", customtest=output)
