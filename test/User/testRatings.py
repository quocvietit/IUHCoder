import requests
import json

reponse = requests.get("http://localhost:3333/api/user/ratings").json()

json_data = json.loads(reponse)
items = json_data['Items']
for i in items:
    print i['UserName'], " - ", i['Rating']
