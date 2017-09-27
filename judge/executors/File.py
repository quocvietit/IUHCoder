class file:
    def __init__(self, fileName):
        self.__fileName = fileName

    def openFile(self, exc):
        return open(self.__fileName, exc)

    def writeFile(self, content):
        try:
            f = self.openFile('w')
            f.write(content)
            f.close()
            return True
        except:
            return False

    def readFile(self):
        try:
            f = self.openFile('r')
            content = f.read()
            f.close()
            return content
        except:
            return False
