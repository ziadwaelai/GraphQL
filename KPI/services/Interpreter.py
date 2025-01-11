from KPI.services.tokens import REGEX, VALUE, PATTERN
from KPI.services.operations import OperatorFactory
class Interpreter:
    def __init__(self, lexer):
        self.lexer = lexer
        self.current_token = self.lexer.get_next_token()

    def eat(self, token_type):
        if self.current_token.type == token_type:
            self.current_token = self.lexer.get_next_token()
        else:
            raise ValueError(f"Unexpected token type. Expected {token_type} but got {self.current_token.type}")

    def parse_expression(self):
        if self.current_token.type == REGEX:
            self.eat(REGEX)
            value = self.current_token.value
            self.eat(VALUE)
            pattern = self.current_token.value
            self.eat(PATTERN)
            operator = OperatorFactory.get_operator("REGEX")
            return operator.execute(value, pattern)

        operator = OperatorFactory.get_operator("ARITHMETIC")
        return operator.execute(self.lexer.text)
