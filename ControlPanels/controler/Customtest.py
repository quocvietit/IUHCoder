from controlPanels.controler.WriteFile import writeFile as wf
from controlPanels.controler.Compile import compile as cp


class customtes:
    def __init__(self, codeText, inputText):
        self.codeText = codeText
        self.inputText = inputText
        self.pathInput = '.\Database\Input\input.txt'
        self.pathCode = '.\Database\FileCode\\file.cpp'
        self.writeToFile()
        self.compile()

    def writeToFile(self):
        wf(self.codeText, self.pathCode)
        wf(self.inputText, self.pathInput)

    def compile(self):
        cp(self.pathCode, self.pathInput)

    def toString(self):
        return open(".\Database\Output\output.txt").read()
