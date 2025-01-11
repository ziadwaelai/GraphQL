from KPI.services.tokens import Token, INTEGER, EOF, TokenFactory

class Lexer:
    def __init__(self, text):
        self.text = text
        self.pos = 0
        self.current_char = self.text[self.pos]

    def error(self):
        raise Exception('Invalid character encountered')

    def advance(self):
        """Advance the `pos` pointer and update `current_char`."""
        self.pos += 1
        if self.pos >= len(self.text):
            self.current_char = None  # End of input
        else:
            self.current_char = self.text[self.pos]

    def skip_whitespace(self):
        """Skip over any whitespace in the input."""
        while self.current_char is not None and self.current_char.isspace():
            self.advance()

    def integer(self):
        """Return a multi-digit integer from the input."""
        result = ''
        while self.current_char is not None and self.current_char.isdigit():
            result += self.current_char
            self.advance()
        return Token(INTEGER, int(result))

    def get_next_token(self):
        if self.pos >= len(self.text):
            return Token(EOF, None)

        current_char = self.text[self.pos]

        # Skip whitespace
        if current_char.isspace():
            self.pos += 1
            return self.get_next_token()

        if self.text[self.pos:].startswith("Regex"):
            self.pos += len("Regex")
            return TokenFactory.create_token("Regex")

        if current_char == '(' or current_char == ',' or current_char == ')':
            self.pos += 1
            return self.get_next_token()  

        if current_char == '"':
            pattern_value = ''
            self.pos += 1  # Skip opening quote
            while self.pos < len(self.text) and self.text[self.pos] != '"':
                pattern_value += self.text[self.pos]
                self.pos += 1
            self.pos += 1 
            return TokenFactory.create_token(f'"{pattern_value}"')

        
        value = ''
        while self.pos < len(self.text) and self.text[self.pos] not in ",) ":
            value += self.text[self.pos]
            self.pos += 1
        return TokenFactory.create_token(value)