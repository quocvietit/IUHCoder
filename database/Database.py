from __future__ import print_function
import boto3


class connection:
    def __init__(self):
        self.__connection = boto3.resource('dynamodb')

    def getConnection(self):
        return self.__connection
