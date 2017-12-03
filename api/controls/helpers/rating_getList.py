"""
@author: Vuong Quoc Viet
@version: 2.0
@since: Nov 18, 2017
"""

from databases.database.database import connection
from controls.entities.table import table
from controls.helpers.jsonFormat import jsonFormat as fm


class rating():
    def __init__(self):
        self.__listRating = connection().getAllItemTable(table('user').getTableName())

    def getListRatingByJson(self):
        return self.__listRating

    def getListRatingByJsonFormat(self):
        return  fm(self.__listRating).format()



