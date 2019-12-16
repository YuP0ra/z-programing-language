import ply.lex as lex
import ply.yacc as yacc

reserved_types = {
        'def'       :'R_DEF',

        'if'        :'R_IF',
        'for'       :'R_FOR',
        'while'     :'R_WHILE',

        'and'       :'R_AND',
        'not'       :'R_NOT',
        'or'        :'R_OR',

        'return'    :'R_RETURN',
    }

tokens = [
    # Identifiers
    'ID',
    # Primitive data types
    'FLOAT',
    # Literals
     "LPAREN", "RPAREN", "COLON", "COMMA", "NEWLINE",
    # Operators
     "PLUS", "MINUS", "MULTIPLY", "DIVIDE", "MOD", "ASSIGN", "EQUAL", "NOTEQUAL",
     ] + list(reserved_types.values())

# Token
t_FLOAT        = r'[+-]?' + r'\d+.\d+'
t_LPAREN       = r'\('
t_RPAREN       = r'\)'
t_COLON        = r'\:'
t_COMMA        = r'\,'
t_MULTIPLY     = r'\*'
t_DIVIDE       = r'\/'
t_PLUS         = r'\+'
t_MINUS        = r'\-'
t_MOD          = r'%'
t_ASSIGN       = r'='
t_EQUAL        = r'=='
t_NOTEQUAL     = r'!='

# Ignored characters
t_ignore = " \t"

def t_ID(t):
    r'[_a-zA-Z]+[_a-zA-Z0-9]*'

    if t.value in reserved_types:
        t.type = reserved_types[t.value]

    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_error(t):
    print("Lexical error at the word: %s" % t.value[0])
    quit()

# Build the lexer
lexer = lex.lex()

var_table = {}

precedence = (
    ('left', 'PLUS', 'MINUS'),
    ('left', 'MULTIPLY', 'DIVIDE'),
)

res = []
def p_s0(t):
    '''
    program     : sourcecode program
                |
    '''

def p_s00(t):
    '''
    sourcecode  : NEWLINE
                | assignment
    '''
    res.append(t[1])


def p_s02(t):
    '''
    assignment  : ID ASSIGN FLOAT
    '''
    t[0] = "float %s = %sf; \n" % (t[1], t[3])


def p_error(t):
    if t:
        print("Syntax error at the word: %s" % t)
    else:
        print("Syntax error .. God only knows where or why!")

parser = yacc.yacc()

cd = """
y = 17.3
"""

parser.parse(cd)
print("".join(res))

# while True:
#     parser.parse(input(">>>"))
