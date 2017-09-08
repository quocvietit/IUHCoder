import os


class writeFile():
    def __init__(self, data):
        self.data = data
        self.writeFile()

    def __call__(self):
        self.writeFile()

    def writeFile(self):
        file = open('./Database/FileCode/file.cpp', 'w')
        file.write(self.data)
        file.close()
