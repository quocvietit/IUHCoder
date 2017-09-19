from flask import Blueprint, render_template, request
from controlPanels.controler.Customtest import customtes as ct

bp = Blueprint(__name__, __name__, template_folder='templates')
output = ""

@bp.route('/customtest', methods=['POST', 'GET'])
def customtest():
    output = None
    if request.method == 'POST':
        if request.form.get('customtest'):
            codeText = request.form.get('mycode')
            inputText = request.form.get('inputtext')
            output = ct(codeText, inputText).toString()
    return render_template("customtest/customtest.html", output=output)
