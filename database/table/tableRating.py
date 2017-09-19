from __future__ import print_function
import boto3

class tableRating:

    def __init__(self):
        self.dynamodb = boto3.resource('dynamodb')
        self.tableName = 'RatingIUHCoder'
        self.create()

    def create(self):
        self.table = self.dynamodb.create_table(
            Att
        )
