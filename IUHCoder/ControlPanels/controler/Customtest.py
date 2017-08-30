from ControlPanels.controler.WriteFile import writeFile as wf
from ControlPanels.controler.Compile import compile as cp


class customtes:
    def __init__(self, codeText, inputText):
        self.codeText = codeText
        self.inputText = inputText
        self.pathInput = '.\Database\Input\input.txt'
        self.pathCode = '.\Database\FileCode\\file.cpp'
        self.__call__()

    def __call__(self, *args, **kwargs):
        self.writeToFile()
        self.compile()

    def writeToFile(self):
        wf(self.codeText, self.pathCode)
        wf(self.inputText, self.pathInput)

    def compile(self):
        cp(self.pathCode, self.pathInput)
