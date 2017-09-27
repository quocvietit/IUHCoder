from  passlib.hash import sha256_crypt
from control.entities.User import user
from control.helper.InfoUser import infoUser

class login:
    def __init__(self, form):
        self.__userName = form['userName']
        self.__password = form['password']

    def getUserName(self):
        return self.__userName

    def getPassword(self):
        return sha256_crypt.hash(self.__password)

    def toString(self):
        return '{} - {} - {}'.format(self.__userName, self.getPassword())

    def checkUser(self):
        person = infoUser().getInfoUser(self.__userName)
        if person == 404 or not sha256_crypt.verify(self.__password, person.getPassword()):
            return False
        return True