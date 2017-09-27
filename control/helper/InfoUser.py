from database.Database import connection as con
from control.entities.User import user


class infoUser:
    def __init__(self):
        self.__table = 'UserIUHCoder'
        pass

    def getInfoUser(self, userName):
        person = con().getItemsTableByKey(self.__table, 'UserName', userName)
        if(len(person)!=2):
            return 404
        return self.parseUser(person['Item'])

    def parseUser(self, items):
        return user(items['UserName'],
                    items['Password'],
                    items['FullName'],
                    items['Age'],
                    items['Phone'],
                    items['Email'],
                    items['Rating'],
                    )
