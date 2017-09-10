from person import person

class user(person):

    def __init__(self, mssvUser, clasUser):
    	super(person).__init__
    	self.mssv = mssvUser
    	self.clas = clasUser
        pass

