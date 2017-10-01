"""
@author: Vuong Quoc Viet
@version: 1.0
@since: Sep 27, 2017
"""

from database.dynamodb.list_rating import ListRating

class Rating:
    
    
    def __init__(self):
        self.__connection = ListRating()

    def get_list(self):
        return self.__connection.get_rating()
        