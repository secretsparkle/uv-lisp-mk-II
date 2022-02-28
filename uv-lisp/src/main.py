import parser
import scanner
import sys


class Error:
    def __init__(self, description):
        self.description = description

    def get_description(self):
        return self.description

class Table:
    def __init__(self):
        self.table = {}

    def access(self, key):
        return self.table[key]

    def insert(self, key, value):
        self.table[key] = value

def main():
    source = ""
    # open source file if supplied
    if len(sys.argv) > 1 and len(sys.argv) < 3:
        f = open(sys.argv[1])
        source = f.read()
        s = scanner.Scanner(source)
        s.split_into_lexemes()
        if s.define_tokens() == False:
            print("Error: No match for Token")
            return

        print(s.tokens)
        for token in s.tokens:
            print(token.token_type)
            p = parser.Parser(s.tokens)
            print(p.is_BODY())

if __name__=="__main__":
    main()