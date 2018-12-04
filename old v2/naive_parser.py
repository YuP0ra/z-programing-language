from rply import ParserGenerator

class Parser():
    def __init__(self):
        self.pg = ParserGenerator([
                    # Identifiers
                    'TYPE_INT', 'TYPE_STRING', 'TYPE_BOOL', 'ID',
                    # Primitive data types
                    'INTEGER', 'STRING', 'BOOL',
                    # Literals
                     "LPAREN", "RPAREN", "LBRACE", "RBRACE", "COLON", "COMMA", "DOT", "SEMICOLON",
                    # Operators
                     "PLUS", "MINUS", "MULTIPLY", "DIVIDE", "MOD", "ASSIGN", "EQUAL", "NOTEQUAL",
                    # Errors
                    "UNKOWN"
            ])

    def parse(self):
        @self.pg.production('expression : TYPE_INT ASSIGN INTEGER SEMICOLON')
        def number(p):
            return Number(p[1].value)

    def get_parser(self):
        return self.pg.build()
