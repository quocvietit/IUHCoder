"""
@author: Vuong Quoc Viet
@version: 2.0
@since: Nov 14, 2017
"""
from __future__ import print_function
from passlib.hash import sha256_crypt
from controls.entities.user import user


class register:
    def __init__(self, userName, password):
        self.__userName = userName
        self.__password = password

    def getUserName(self):
        return self.__userName

    def getPassword(self):
        return sha256_crypt.hash(self.__password)

    def toString(self):
        return 'User name: {}\
                Password: {}\n'.format(self.getUserName(),
                                       self.getPassword())

    def registerUser(self):
        return user(self.__userName, self.getPassword()).create()
