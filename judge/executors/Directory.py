import os
import shutil


class directory:
    def __init__(self, directoryName):
        self.__directoryName = directoryName

    def createDir(self):
        try:
            if os.path.exists(self.__directoryName):
                self.deleteDir()
            os.mkdir(self.__directoryName)
            return True
        except:
            return False

    def deleteDir(self):
        try:
            if os.path.exists(self.__directoryName):
                shutil.rmtree(self.__directoryName)
            return True
        except:
            return False
