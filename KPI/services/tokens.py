INTEGER, PLUS, MINUS, MULTIPLY, DIVIDE, POWER, REGEX, VALUE, PATTERN, EOF = (
    'INTEGER', 'PLUS', 'MINUS', 'MULTIPLY', 'DIVIDE', 'POWER', 'REGEX', 'VALUE', 'PATTERN', 'EOF'
)

class Token:
    def __init__(self, type, value):
        self.type = type
        self.value = value

    def __str__(self):
        return f"Token({self.type}, {repr(self.value)})"

    def __repr__(self):
        return self.__str__()

class TokenFactory:
    @staticmethod
    def create_token(text):
        if text.isdigit():
            return Token(INTEGER, int(text))
        elif text == '+':
            return Token(PLUS, text)
        elif text == '-':
            return Token(MINUS, text)
        elif text == '*':
            return Token(MULTIPLY, text)
        elif text == '/':
            return Token(DIVIDE, text)
        elif text == '^':
            return Token(POWER, text)
        elif text == "Regex":
            return Token(REGEX, text)
        elif text.startswith('"') and text.endswith('"'):
            return Token(PATTERN, text[1:-1])  # Remove quotes
        else:
            return Token(VALUE, text.strip())
