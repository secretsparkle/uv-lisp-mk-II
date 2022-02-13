from scanner import Token
from scanner import TokenType

class Parser:
    def __init__(self, tokens):
        self.current = 0
        self.tokens = tokens

    def is_ATOM(self):
        print("atom")
        if self.is_NUMBER() or self.is_KEYWORD_IDENTIFIER or self.is_IDENTIFIER() or self.is_STRING():
            return True
        else:
            return False

    def is_BODY(self):
        print("body")
        while self.is_S_EXPRESSION():
            continue
        if self.is_EOF():
            return True
        else:
            return False

    def is_EOF(self):
        print("eof")
        if self.tokens[self.current].token_type == TokenType.EOF:
            return True
        else:
            return False

    def is_IDENTIFIER(self):
        print("identifier")
        if self.tokens[self.current].token_type == TokenType.IDENTIFIER:
            self.next_token()
            return True
        else:
            return False

    def is_KEYWORD_IDENTIFIER(self):
        print("keyword")
        if self.tokens[self.current].token_type == TokenType.KEYWORD_IDENTIFIER:
            self.next_token()
            return True
        else:
            return False

    def is_LEFT_PAREN(self):
        print("left paren")
        if self.tokens[self.current].token_type == TokenType.LEFT_PAREN:
            self.next_token()
            return True
        else:
            return False

    def is_LIST(self):
        print("list")
        if not self.is_LEFT_PAREN():
            return False
        while self.is_S_EXPRESSION():
            continue
        if not self.is_RIGHT_PAREN():
            return False

        return True

    def is_NUMBER(self):
        print("number")
        print(self.current)
        if self.tokens[self.current].token_type == TokenType.NUMBER:
            self.next_token()
            return True
        else:
            return False

    def is_RIGHT_PAREN(self):
        print("right paren")
        if self.tokens[self.current].token_type == TokenType.RIGHT_PAREN:
            self.next_token()
            return True
        else:
            return False

    def is_S_EXPRESSION(self):
        print("s expression")
        if self.is_LIST() or self.is_ATOM():
            return True
        else:
            return False

    def is_STRING(self):
        print("string")
        if self.tokens[self.current].token_type == TokenType.STRING:
            self.next_token()
            return True
        else:
            return False

    def next_token(self):
        self.current += 1
