"""
@author: Vuong Quoc Viet
@version: 2.0
@since: Nov 18, 2017
"""
from __future__ import print_function

TABLE = {'user': 'UserIUHCoder'}

class table():
    def __init__(self, tableName):
        self.__tableName = tableName

    def getTableName(self):
        return TABLE[self.__tableName]

    def toString(self):
        return TABLE
