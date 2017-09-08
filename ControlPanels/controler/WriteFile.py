class writeFile:
    def __init__(self, data, path):
        self.data = data
        self.path = path
        self.writeFile()

    def __call__(self):
        self.writeFile()

    def writeFile(self):
        try:
            self.file = open(self.path, 'w')
            self.file.write(self.data)
            self.file.close()
        except IOError as e:
            print('adad', e)
