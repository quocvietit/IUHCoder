import requests

data = {
    "username": "Test1",
     "password": "123"
}
reponse = requests.post("http://localhost:3333/api/user/login",json=data).json()
if(reponse['status']=='True'):
     print ("Login Done!")
else:
     print ("Error")
