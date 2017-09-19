from __future__ import print_function
import boto3

dynamobd = boto3.resource('dynamodb')

table = dynamobd.create_table(
    AttributeDefinitions=[
        {
            'AttributeName': 'username',
            'AttributeType': 'S'
        },
        {
            'AttributeName': 'password',
            'AttributeType': 'S'
        },
    ],
    TableName='UserIUHCoder',
    KeySchema=[
        {
            'AttributeName': 'username',
            'KeyType': 'HASH'
        },
{
            'AttributeName': 'password',
            'KeyType': 'RANGE'
        }
    ],
    ProvisionedThroughput={
        'ReadCapacityUnits': 5,
        'WriteCapacityUnits': 5
    }
)

print("Table Status: ", table.table_status)
