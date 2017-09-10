class person:

    def __init__(self, idPerson, namePerson, phonePerson="", emailPerson="", agePersion=0):
        self.id = idPerson
        self.name = namePerson
        self.phone = phonePerson
        self.email = emailPerson
        self.age = agePersion

    def toString(self):
        print "{} - {}".format(self.id, self.name)