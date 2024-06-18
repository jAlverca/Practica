from controls.tda.stack.stackOperations import StackOperations

class Stack():
    def __init__(self, tope):
        self.__stack = StackOperations(tope)

    def push(self, data):
        self.__stack.push(data)

    def pop(self):
        return self.__stack.pop
    
    @property
    def print(self):
        self.__stack.print
    
    def verify(self):
        return self.__stack.verifyTop