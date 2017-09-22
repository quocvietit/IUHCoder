from __future__ import print_function
from botocore.exceptions import ClientError
import boto3


class connection:
    def __init__(self):
        self.__connection = boto3.resource('dynamodb')

    def getConnection(self):
        return self.__connection

    def getConnectionTable(self, table):
        return self.getConnection().Table(table)

    def getItemsTableByKey(self, table, key, valueKey):
        try:
            response = self.getConnectionTable(table).get_item(
                Key={
                    key: valueKey,
                }
            )
        except ClientError as e:
            return 404
        else:
            return response
