from __future__ import print_function
from botocore.exceptions import ClientError
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('UserIUHCoder')
response = table.scan()
item = response['Items']
for i in item:
    print (i['UserName']," ",i['Rating'])