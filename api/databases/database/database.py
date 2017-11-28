"""
@author: Vuong Quoc Viet
@version: 2.0
@since: Nov 14, 2017
"""

from __future__ import print_function
from botocore.exceptions import ClientError
import boto3


class connection():
    def __init__(self):
        self.__connection = boto3.resource('dynamodb')

    def getConnection(self):
        return self.__connection

    def getConnectionTable(self, table):
        return self.getConnection().Table(table)

    def getItemsTableByKey(self, table, key, value):
        try:
            response = self.getConnectionTable(table).get_item(
                Key={
                    key: value,
                }
            )
        except ClientError as e:
            return 404
        else:
            return response

    def getAllItemTable(self, table):
        try:
            response = self.getConnectionTable(table).scan()
        except ClientError as e:
            return 404
        else:
            return response
