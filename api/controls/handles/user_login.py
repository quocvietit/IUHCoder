"""
@author: Vuong Quoc Viet
@version: 2.0
@since: Nov 14, 2017
"""
from  passlib.hash import sha256_crypt
from api.controls.helpers.user_getInformation import inforUser


class login():
    def __init__(self, userName, password):
        self.__userName = userName
        self.__password = password

    def getUserName(self):
        return self.__userName

    def getPassword(self):
        return sha256_crypt.hash(self.__password)

    def toString(self):
        return '{} - {} - {}'.format(self.__userName, self.getPassword())

    def checkUser(self):
        data = inforUser(self.__userName).getUser()
        if data == 404 or not sha256_crypt.verify(self.__password, data.getPassword()):
            return False
        return True
