"""
@author: Vuong Quoc Viet
@version: 1.0
@since: Sep 27, 2017
"""

from __future__ import print_function
from database.Database import connection

TABLE = "UserIUHCoder"
class ListRating:

    
    def __init__(self):
        self.__connection = connection().getConnectionTable("UserIUHCoder")
        
    def get_rating(self):
        print (self.__connection.scan())
        try:
            response = self.__connection.scan()
            return response['Items']
        except:
            return 404

