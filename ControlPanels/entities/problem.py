class problem:
    def __init__(self, idProblem, name, content, level, algorithm, input, output):
        self.id = idProblem
        self.name = name
        self.content = content
        self.level = level
        self.algorithm = algorithm
        self.input = input
        self.output = output

    def toString(self):
        print "{} - {}".format(self.id, self.name)

