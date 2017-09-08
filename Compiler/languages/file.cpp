from Language import language
import os
import filecmp

codes = {200:'AC', 201:'WA', 202:'Compile Error',404:'file not found',400:'error',408:'timeout'}

class CPP():

    def __init__(self, fileName, input, result):
        self.file = fileName
        self.input = input
        self.output = 'output.txt'
        self.result = result


    def compile(self):
        file = self.file[:-5]
        #True = 0 or False = 1
        compile_File = os.system('g++ -o {0} {1}'.format(file, self.file))
        if compile_File == 1:
            return 202
        os.system('{0} < {1} > {2}'.format(file, self.input, self.output))
        if os.path.isfile(self.output):
            pass
        if filecmp.cmp(self.result, self.output):
            return 200
        return 201

    def excute(self):
        pass

a = CPP('Demo.cpp','input.txt', 'result.txt')
print codes[a.compile()]
