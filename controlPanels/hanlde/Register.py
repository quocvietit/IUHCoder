from  passlib.hash import sha256_crypt
from controlPanels.entities.User import user


class register:
    def __init__(self, form):
        self.__userName = form['userName']
        self.__password = form['password']
        self.__confirmPassword = form['confirmPassword']

    def getUserName(self):
        return self.__userName

    def getPassword(self):
        return sha256_crypt.hash(self.__password)

    def toString(self):
        return '{} - {} - {}'.format(self.__userName, self.getPassword(), self.__confirmPassword)

    def checkPassword(self):
        return (self.__password == self.__confirmPassword)

    def registerUser(self):
        return user(self.__userName, self.getPassword()).create()
