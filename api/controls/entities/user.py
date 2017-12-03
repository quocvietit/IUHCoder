"""
@author: Vuong Quoc Viet
@version: 2.0
@since: Nov 14, 2017
"""
from __future__ import print_function
from databases.database.database import connection
from controls.entities.table import table
from boto3.dynamodb.conditions import Key


class user():
    def __init__(self, userName, password = None, fullName=None, age=0, phone=None, email=None, rating=0):
        self.__userName = userName
        self.__password = password
        self.__fullName = fullName
        self.__age = age
        self.__phone = phone
        self.__email = email
        self.__rating = rating
        self.__table = table('user').getTableName()

    def getUserName(self):
        return self.__userName

    def getPassword(self):
        return self.__password

    def setPassword(self, password):
        self.__password = password

    def getFullName(self):
        return self.__fullName

    def setFullName(self, fullName):
        self.__fullName = fullName

    def getAge(self):
        return self.__age

    def setAge(self, age):
        self.__age = age

    def getPhone(self):
        return self.__phone

    def setPhone(self, phone):
        self.__phone = phone

    def getEmail(self):
        return self.__email

    def setEmail(self, email):
        self.__email = email

    def getRating(self):
        return self.__rating

    def setRating(self, rating):
        self.__rating = rating

    def getTable(self):
        return self.__table

    def toString(self):
        return "User name: {}\
                Password: {}\
                Full name: {}\
                Age: {}\
                Phone: {}\
                Email: {}\
                Rating: {}\n".format(self.__userName,
                                     self.__password,
                                     self.__fullName,
                                     self.__age,
                                     self.__phone,
                                     self.__email,
                                     self.__rating)

    # create User
    def create(self):
        try:
            con = connection()
            dynamodb = con.getConnection()
            table = dynamodb.Table(self.__table)

            response = table.query(
                KeyConditionExpression=Key('UserName').eq(self.__userName)
            )

            if (len(response['Items']) != 0):
                return False

            table.put_item(
                Item={
                    'UserName': self.__userName,
                    'Password': self.__password,
                    'Rating': self.__rating,
                }
            )
            return True

        except:
            return False

    # update --
    def update(self, data):
        try:
            con = connection()
            dynamodb = con.getConnection()
            table = dynamodb.Table(self.__table)

            query = "set "
            value = {}
            cnt = 1
            print(data)
            for key in data.keys():
                query += key + " = :val" + str(cnt) + ", "
                value[':val' + str(cnt)] = data[key]
                cnt += 1

            query = query[:-2]
            table.update_item(
                Key={
                    'UserName': self.__userName
                },
                UpdateExpression=query,
                ExpressionAttributeValues=value
            )
            return True

        except:
            return False