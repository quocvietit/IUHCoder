"""
@author: Vuong Quoc Viet
@version: 1.0
@since: Sep 27, 2017
"""

from __future__ import print_function
from database.Database import connection

class ListRating:
    TABLE = "UserIUHCoder"
    
    def __init__(self):
        self.__connection = connection.getConnectionTable(TABLE)
        
    def get_rating(self):
        try:
            response = self.__connection.scan()
            return response['Items']
        except:
            return 404

