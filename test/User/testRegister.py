import requests

userName = "Test"
password = "123"
count = 0
for i in range(1,1001):
    data = {
        "username":userName+str(i),
        "password":password
    }
    x = requests.post("http://localhost/api/user/register",json=data).json()
    if(x['status']=='True'):
        count+=1
    print "TEST"+str(i)+": "+str(x['status'])

print "RES: "+count+"/1000"