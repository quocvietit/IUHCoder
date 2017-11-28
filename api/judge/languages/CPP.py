"""
@author: Vuong Quoc Viet
@version: 2.0
@since: Nov 23, 2017
"""
import os


class CPP():
    def __init__(self, fileName):
        self.__fileName = fileName
        self.__classFile = fileName[:-4]

    def compile(self):
        try:
            if not os.path.isfile(self.__fileName):
                return 404

            if os.path.isfile(self.__classFile):
                os.remove(self.__classFile)

            # True = 0 or False = 1
            cmd = os.system('g++ -o {} {}'.format(self.__classFile, self.__fileName))

            if cmd == 1 or not os.path.isfile(self.__classFile):
                return 202
            return 200
        except:
            return 400

    def getCMD(self):
        return '{} < {} > {}'
