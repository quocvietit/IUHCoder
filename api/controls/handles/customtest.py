"""
@author: Vuong Quoc Viet
@version: 2.0
@since: Nov 23, 2017
"""

from api.judge.hanlde.actions import actions
from api.controls.entities.task import task


class customtest:
    def __init__(self, userName, sourceCode, input, language):
        self.__userName = userName
        self.__sourceCode = sourceCode
        self.__input = input
        self.__language = language

    def getOutput(self):
        cmd = actions(task(self.__userName, self.__sourceCode, self.__language))
        if not cmd.getCommpile():
            cmd.clear()
            return 'Compiler Error!'
        else:
            res = cmd.getResult(self.__input)
            cmd.clear()
            if res == 400 or res == 404:
                return 'Runtime Error!'
            else:
                return res
