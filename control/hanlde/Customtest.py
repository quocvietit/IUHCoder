from judge.hanlde.Actions import actions
from control.entities.Task import task
import os


class customtest:
    def __init__(self, form, userName):
        self.__sourceCode = form['sourceCode']
        self.__input = form['input']
        self.__output = None
        self.__userName = userName

    def getOutput(self):
        cmd = actions(task(self.__userName, self.__sourceCode, 'C++'))
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
