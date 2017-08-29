from flask import Blueprint, render_template, request
from Compiler.Languages.writeFile import writeFile as wf

bp = Blueprint(__name__, __name__, template_folder='templates')


@bp.route('/customtest', methods=['POST', 'GET'])
def show():
    if request.method == 'POST':
        if request.form.get('customtest'):
            text = request.form.get('codetext')
            wf(text)

    return render_template("customtest.html")
