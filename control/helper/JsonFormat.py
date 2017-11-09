"""
@author: Vuong Quoc Viet
@version: 2.0
@since: Nov 9, 2017
"""
import json
import decimal

# Helper class to convert a DynamoDB item to JSON.
class DecimalEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, decimal.Decimal):
            if o % 1 > 0:
                return float(o)
            else:
                return int(o)
        return super(DecimalEncoder, self).default(o)


class jsonFormat:
    def __init__(self, jsonData):
        self.__jsonData = jsonData

    def format(self):
        return json.dumps(self.__jsonData, indent=5, cls= DecimalEncoder)