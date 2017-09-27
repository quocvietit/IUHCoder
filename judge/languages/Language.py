from judge.languages.C import C
from judge.languages.CPP import CPP


class language:
    def __init__(self, fileName, language):
        self.__fileName = fileName
        self.__language = language

    def compiler(self):
        if self.__language == 'C':
            return C(self.__fileName).compile()
        elif self.__language == 'C++':
            return CPP(self.__fileName).compile()
        elif self.__language == 'Python':
            pass

    def getCMD(self):
        if self.__language == 'C':
            return C(self.__fileName).getCMD()
        elif self.__language == 'C++':
            return CPP(self.__fileName).getCMD()
        elif self.__language == 'Python':
            pass
