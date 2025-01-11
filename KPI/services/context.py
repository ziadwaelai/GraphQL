from KPI.services.lexer import Lexer
from KPI.services.Interpreter import Interpreter

class Context:
    def __init__(self, expression):
        self.lexer = Lexer(expression)
        self.interpreter = Interpreter(self.lexer)

    def evaluate(self):
        return self.interpreter.parse_expression()
