from controlPanels.entities.Entrance import entrance
class customtest(entrance):

	def __init__(self):
		self.id = id
		self.code = code
		self.language = language
		self.input = input

	def toString(self):
		return  "{} - {}".format(self.id, self.getOutPut())

	def getOutPut(self):
		return  