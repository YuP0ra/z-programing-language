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

        'true'      :'BOOL',
        'false'     :'BOOL',

        'return'    :'R_RETURN',

    }

tokens = [
    # Identifiers
    'ID',
    # Primitive data types
    'INTEGER', 'FLOAT', 'STRING',
    # Literals
     "LPAREN", "RPAREN", "COLON", "COMMA", "NEWLINE",
    # Operators
     "PLUS", "MINUS", "MULTIPLY", "DIVIDE", "MOD", "ASSIGN", "EQUAL", "NOTEQUAL",
     ] + list(reserved_types.values())

# Token
t_FLOAT        = r'[+-]?' + r'\d+.\d+'
t_INTEGER      = r'[+-]?' + r'\d+'
t_STRING       = r'".*"'
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


def p_cool(t):
    '''
    program     : sourcecode program
                |

    sourcecode  : NEWLINE
                | assignment
                | declaration
                | methodcall
                | returnfunc
                | decision
                | loop



    assignment  : ID ASSIGN idexpr
                | ID

    idexpr      : value  mathopt  idexpr
                | value

    value       : ID
                | BOOL
                | STRING
                | expression
                | methodcall



    declaration : R_DEF  ID  LPAREN  args  RPAREN  COLON

    args        : ID  COMMA  args
                | ID
                |



    methodcall  : ID  LPAREN  callargs  RPAREN

    callargs    : value  COMMA  callargs
                | value
                |



    returnfunc  : R_RETURN
                | R_RETURN value



    expression  : LPAREN  expression  RPAREN
                | num  mathopt  expression
                | num

    num         : INTEGER
                | FLOAT

    mathopt     : PLUS
                | MINUS
                | MULTIPLY
                | DIVIDE
                | MOD



    decision    : R_IF  condition  COLON

    loop        : R_WHILE  condition  COLON

    condition   : BOOL
                | ID  condopt  value
                | LPAREN  condition  RPAREN
                | condition  condexpend  condition

    condopt     : EQUAL
                | NOTEQUAL

    condexpend  : R_AND
                | R_NOT
                | R_OR


    '''


def p_error(t):
    if t:
        print("Syntax error at the word: %s" % t)
    else:
        print("Syntax error .. God only knows where or why!")

parser = yacc.yacc()

cd = """
x = 5
y = x + 17.3

soso = "text"

def p(t):
    if x != y:
        return "Syntax error at the word"

    if t == false:
        print("Syntax error .. God only knows where or why!")

    return
"""

parser.parse(cd)
print("\nFinished.")

# while True:
#     parser.parse(input(">>>"))
