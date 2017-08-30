class person:

    def __init__(self, id, name):
        self.id = id
        self.name = name

    def toString(self):
        print "{} - {}".format(self.id, self.name)