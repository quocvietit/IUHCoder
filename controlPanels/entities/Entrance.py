class entrance:
    def __init__(self, id, code, lang):
        self.__id = id
        self.__code = code
        self.__lang = lang

    def getId(self):
        return self.__id

    def setId(self, id):
        self.__id

    def getCode(self):
        return self.__code

    def setCode(self, code):
        self.__code = code

    def getLang(self):
        return self.__lang

    def setLang(self, lang):
        self.__lang = lang

    def toString(self):
        return "{} - {} - {}".format(self.__id, self.__code, self.__lang)

