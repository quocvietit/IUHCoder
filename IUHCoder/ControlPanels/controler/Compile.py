import os

codes = {200: 'AC', 201: 'WA', 202: 'Compile Error', 404: 'file not found', 400: 'error', 408: 'timeout'}


class compile:
    def __init__(self, fileName, input ):
        self.fileName = fileName
        self.input = input
        self.output = '.\Database\Output\output.txt'
        self.__call__()

    def __call__(self, *args, **kwargs):
        self.compile()

    def compile(self):
        file = self.fileName[:-4]
        # True = 0 or False = 1
        compile_File = os.system('g++ -o {} {}'.format(file, self.fileName))
        if compile_File == 1:
            return 202
        os.system('{} < {} > {}'.format(file, self.input, self.output))
        if os.path.isfile(self.output):
            pass
