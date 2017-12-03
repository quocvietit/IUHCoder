"""
@author: Vuong Quoc Viet
@version: 1.1
@since: Sep 27, 2017
"""

from flask import Blueprint, render_template
from IP import ip
import requests
import json

bp = Blueprint(__name__, __name__, template_folder='templates')

IP = ip().getIP()

@bp.route('/rating')
def rating():
    try:
        reponse = requests.get("http://"+IP+":3333/api/user/ratings").json()
        json_data = json.loads(reponse)
        items = json_data['Items']
    except:
        pass
    else:
        return render_template('dashboard/rating.html', ratings=items)
    return render_template('dashboard/rating.html')
