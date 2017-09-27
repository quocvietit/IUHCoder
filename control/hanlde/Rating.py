"""
@author: Vuong Quoc Viet
@version: 1.0
@since: Sep 27, 2017
"""

from database.dynamodb.list_rating import ListRating

class Rating:
    
    
    def __init__(self):
        return ListRating.get_rating()
        