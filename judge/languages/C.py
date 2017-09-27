import os


class C():
    def __init__(self, fileName):
        self.__fileName = fileName

    def compile(self):
        try:
            if not os.path.isfile(self.__fileName):
                return 404

            classFile = self.__fileName[:-5]

            if os.path.isfile(classFile):
                os.remove(classFile)

            # True = 0 or False = 1
            fileCompiler = os.system('g -o {} {}'.format(classFile, self.__fileName))

            if fileCompiler == 1 or not os.path.isfile(classFile):
                return 202
            return 200
        except:
            return 400

    def getCMD(self):
        return './{} < {} > {}'
