"""
@author: Vuong Quoc Viet
@version: 2.0
@since: Nov 14, 2017
"""

from __future__ import print_function
from databases.database.database import connection as con
from controls.entities.user import user
from controls.helpers.jsonFormat import jsonFormat as fm


class inforUser():
    def __init__(self, userName):
        self.__userName = userName
        self.__table = 'UserIUHCoder'

    def getInfoUser(self):
        data = con().getItemsTableByKey(self.__table, 'UserName', self.__userName)
        if (len(data) != 2):
            return 404
        return data['Item']

    def getUser(self):
        items = self.getInfoUser()
        if( items == 404):
            return 404
        return user(items['UserName'],
                    items['Password'],
                    items['FullName'],
                    items['Age'],
                    items['Phone'],
                    items['Email'],
                    items['Rating'])

    def getJson(self):
        return self.getInfoUser()

    def getJsonFormat(self):
        return fm(self.getInfoUser()).format()