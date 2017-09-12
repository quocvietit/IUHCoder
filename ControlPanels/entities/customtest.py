class customtest:

	def __init__(self, id, code, language, input):
		self.id = id
		self.code = code
		self.language = language
		self.input = input

	def toString(self):
		return  "{} - {}".format(self.id, self.getOutPut())

	def getOutPut(self):
		return  