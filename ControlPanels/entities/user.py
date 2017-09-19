from database.Database import connection
from boto3.dynamodb.conditions import Key


class user:
    def __init__(self, userName, password, fullName=None, age=0, phone=None, email=None):
        self.__userName = userName
        self.__password = password
        self.__fullName = fullName
        self.__age = age
        self.__phone = phone
        self.__email = email
        self.__table = 'UserIUHCoder'

    def getUserName(self):
        return self.__userName

    def getPassword(self):
        return self.__password

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

    def toString(self):
        return "{} - {} - {} - {} - {} - {}".format(self.__userName, self.__password, self.__fullName, self.__age,
                                                    self.__phone, self.__email)

    def addUser(self):
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
                    'FullName': self.__fullName,
                    'Age': self.__age,
                    'Phone': self.__phone,
                    'Email': self.__email,
                }
            )
            return True

        except:
            return False
