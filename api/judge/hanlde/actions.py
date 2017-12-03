"""
@author: Vuong Quoc Viet
@version: 2.0
@since: Nov 23, 2017
"""
from judge.languages.language import language
from judge.executors.file import file
from judge.executors.directory import directory
import os
import filecmp

typeLanguage = {'C': '.c', 'C++': '.cpp', 'Java': '.java', "Python": '.py', "Python3": '.py'}


class actions:
    def __init__(self, task):
        self.__task = task
        self.__taskName = str(task.getIdTask())

    def writeCode(self):
        dir = directory(self.__taskName)

        # Create dir
        if (dir.createDir()):
            os.chdir(self.__taskName)

            f = file(self.__taskName + typeLanguage[self.__task.getLanguage()])

            # create and write file
            return f.writeFile(self.__task.getSourceCode())
        return False

    def getCommpile(self):
        if (self.writeCode()):
            f = str(self.__taskName + typeLanguage[self.__task.getLanguage()])
            cp = language(f, self.__task.getLanguage())
            return cp.compiler()
        return False

    def getResult(self, input):
        finName = self.__taskName + '_in'
        foutName = self.__taskName + '_out'

        f = str(self.__taskName + typeLanguage[self.__task.getLanguage()])
        cp = language(f, self.__task.getLanguage())

        try:
            if os.path.isfile(finName):
                os.remove(finName)
            if os.path.isfile(foutName):
                os.remove(foutName)

            fin = file(finName)
            fin.writeFile(input)

            file(foutName).openFile('w')

            cmd = cp.getCMD()

            res = os.system(cmd.format(self.__taskName, finName, foutName))

            if res == 1:
                return 400

            result = file(foutName).readFile()

            os.remove(finName)
            os.remove(foutName)

            return result
        except IOError as e:
            return 400

    def getListResults(self, listInput, listResult):
        listOutput = []

        finName = self.__taskName + '_in'
        foutName = self.__taskName + '_out'
        fresName = self.__taskName + '_res'

        f = str(self.__taskName + typeLanguage[self.__task.getLanguage()])
        cp = language(f, self.__task.getLanguage())
        for i in range(0, len(listInput)):
            try:
                if os.path.isfile(finName):
                    os.remove(finName)
                if os.path.isfile(foutName):
                    os.remove(foutName)

                fin = file(finName)
                fin.writeFile(listInput[i])

                fres = file(fresName)
                fres.writeFile(listResult[i])

                file(foutName).openFile('w')

                cmd = cp.getCMD()

                res = os.system(cmd.format(self.__taskName, finName, foutName))

                if res == 1:
                    return 400

                listOutput.append(file(foutName).readFile())
                file(foutName).writeFile(listOutput[i])
                flag = filecmp.cmp(fresName, foutName)

                os.remove(finName)
                os.remove(foutName)
                os.remove(fresName)

                if not flag:
                    return i

            except IOError as e:
                return 400
        return 200

    def clear(self):
        os.chdir("..")
        try:
            return directory(self.__taskName).deleteDir()
        except IOError as e:
            return False
