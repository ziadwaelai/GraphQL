import re
from abc import ABC, abstractmethod

class Operator(ABC):
    @abstractmethod
    def execute(self, *args):
        pass

class RegexOperator(Operator):
    def execute(self, value, pattern):
        return bool(re.match(pattern, value))

class ArithmeticOperator(Operator):
    def execute(self, expression):
        try:
            result = eval(expression)
            return result
        except Exception as e:
            print(expression)
            raise ValueError(f"Error evaluating arithmetic expression: {e}")

class OperatorFactory:
    OPERATORS = {
        "REGEX": RegexOperator,
        "ARITHMETIC": ArithmeticOperator,
    }

    @staticmethod
    def get_operator(token_type):
        operator_class = OperatorFactory.OPERATORS.get(token_type)
        if operator_class is None:
            raise ValueError(f"Unknown operator for token type: {token_type}")
        return operator_class()
