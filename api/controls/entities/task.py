"""
@author: Vuong Quoc Viet
@version: 2.0
@since: Nov 23, 2017
"""


class task():
    def __init__(self, idTask, sourceCode, language, timeOut=1):
        self.__idTask = idTask
        self.__sourceCode = sourceCode
        self.__language = language
        self.__timeOut = timeOut

    def getIdTask(self):
        return self.__idTask

    def setIdTask(self, idTask):
        self.__idTask = idTask

    def getSourceCode(self):
        return self.__sourceCode

    def setSourceCode(self, sourceCode):
        self.__sourceCode = sourceCode

    def getLanguage(self):
        return self.__language

    def setLanguage(self, language):
        self.__language = language

    def toString(self):
        return "Id Task: {}\
                Soucre Code: {}\
                Languages: {}\
                Time Out: {}\n".format(self.__idTask,
                                       self.__sourceCode,
                                       self.__language,
                                       self.__timeOut)
