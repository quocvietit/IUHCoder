from  passlib.hash import sha256_crypt


class registrationForm:
    def __init__(self, userName, password, confirmPassword):
        self.__userName = userName
        self.__password = password
        self.__confirmPassword = confirmPassword

    def getUserName(self):
        return self.__userName

    def getPassword(self):
        return sha256_crypt.hash(self.__password)

    def checkPassword(self):
        return (self.__password==self.__confirmPassword)

    def toString(self):
        return '{} - {} - {}'.format(self.__userName, self.getPassword(), self.__confirmPassword)
