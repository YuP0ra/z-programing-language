import re

class Scanner:
    def __init__(self,):
        tokens = [
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
             ]

        tokens_patterns = {
            "TYPE_INT"          : r'int',
            "TYPE_STRING"       : r'string',
            "TYPE_BOOL"         : r'bool',

            "ID"                : r'[_a-zA-Z]+[_a-zA-Z0-9]*',

            "INTEGER"           : r'[+-]?' + r'\d+',
            "STRING"            : r'"(.*|@SPACE@)+"',
            "BOOL"              : r'(true)|(false)',

            "LPAREN"            : r'\(',
            "RPAREN"            : r'\)',
            "LBRACE"            : r'\{',
            "RBRACE"            : r'\}',
            "COLON"             : r'\:',
            "COMMA"             : r'\,',
            "DOT"               : r'\.',
            "SEMICOLON"         : r'\;',

            "MULTIPLY"          : r'\*',
            "DIVIDE"            : r'\/',
            "PLUS"              : r'\+',
            "MINUS"             : r'\-',
            "MOD"               : r'%',
            "ASSIGN"            : r'=',

            "EQUAL"             : r'==',
            "NOTEQUAL"          : r'!=',
        }

        # compile the tokens to be used later
        self._tokens = [(k, re.compile(tokens_patterns[k])) for k in tokens_patterns]
        self._source_code = ''

    def set_source_code(self, string):
        # process the sourcecode and remove the Comments
        for match in re.finditer(re.compile(r'".*"'), string):
            inner_string = string[match.span()[0]: match.span()[1]]
            string = string.replace(inner_string, inner_string.replace(' ', '@SPACE@'))

        self._source_code = string


    def next(self):
        for line_number, line in enumerate(self._source_code.split('\n')):
            for word in line.split():
                matched = False

                for token_name, pattern in self._tokens:
                    re_match_result = re.search(pattern, word)
                    if re_match_result and re_match_result[0] == word:

                        if token_name == 'STRING':
                            word = word[1:-1].replace('@SPACE@', ' ')

                        yield (token_name, word, line_number + 1)
                        matched = True
                        break

                if not matched:
                    yield ('UNKOWN', word, line_number + 1)
