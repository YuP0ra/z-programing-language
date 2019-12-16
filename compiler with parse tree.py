import numpy as np
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

        'true'      :'BOOL',
        'false'     :'BOOL',
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


precedence = (
    ('nonassoc', 'R_AND', 'R_NOT', 'R_OR'),
    ('left', 'PLUS', 'MINUS'),
    ('left', 'MULTIPLY', 'DIVIDE'),
)

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


def p_main(t):
    '''
    parsetree   : program
    '''
    print(t[1])


def p_0(t):
    '''
    program     : line program
                |
    '''
    if len(t) == 3:
        if t[2] == None:
            t[0] = t[1]
        else:
            t[0] = (t[1], t[2])
    else:
        t[0] = None


def p_00(t):
    '''
    line        : NEWLINE
                | assignment
                | declaration
                | methodcall
                | returnfunc
                | decision
                | loop
    '''
    t[0] = t[1]


def p_01(t):
    '''
    assignment  : ID ASSIGN idexpr
                | ID
    '''
    if len(t) == 4:
        t[0] = ('ASSIGNMENT', t[1], t[3])
    else:
        t[0] = ('ASSIGNMENT', t[1], 'DEFULT')


def p_02(t):
    '''
    idexpr      : value  mathopt  idexpr
                | value
    '''
    if len(t) == 4:
        t[0] = (t[2], t[1], t[3])
    else:
        t[0] =  t[1]


def p_03(t):
    '''
    value       : ID
                | BOOL
                | STRING
                | expression
                | methodcall
    '''
    t[0] = t[1]


def p_04(t):
    '''
    declaration : R_DEF  ID  LPAREN  args  RPAREN  COLON  LPAREN  program  RPAREN
    '''
    t[0] = ('FUNCTION DECLERATION', ('NAME', t[2]), ('ARGS', t[4]), ('BODY', t[8]))


def p_05(t):
    '''
    args        : args  COMMA  args
                | ID
                |
    '''
    if len(t) == 4:
        for a in t[3]:
            t[1].append(a)
        t[0] = t[1]
    elif len(t) == 2:
        t[0] = [t[1]]
    else:
        t[0] = None

def p_06(t):
    '''
    methodcall  : ID  LPAREN  callargs  RPAREN
    '''
    t[0] = ('FUNCTION CALL', ('NAME', t[1]), ('ARGS', t[3]))


def p_07(t):
    '''
    callargs    : callargs  COMMA  callargs
                | value
                |
    '''
    if len(t) == 4:
        for a in t[3]:
            t[1].append(a)
        t[0] = t[1]
    elif len(t) == 2:
        t[0] = [t[1]]
    else:
        t[0] = None


def p_08(t):
    '''
    returnfunc  : R_RETURN
                | R_RETURN value
    '''
    if len(t) == 3:
        t[0] =  t[2]


def p_09(t):
    '''
    expression  : expression  mathopt  expression
                | LPAREN  expression  RPAREN
                | num
    '''
    if len(t) == 4:
        if t[1] == '(':
            t[0] = (t[2])
        else:
            t[0] = (t[2], t[1], t[3])
    else:
        t[0] =  t[1]


def p_10(t):
    '''
    num         : INTEGER
                | FLOAT
    '''
    t[0] = float(t[1])


def p_11(t):
    '''
    mathopt     : PLUS
                | MINUS
                | MULTIPLY
                | DIVIDE
                | MOD
    '''
    t[0] = t[1]


def p_12(t):
    '''
    decision    : R_IF  condition  COLON  LPAREN  program  RPAREN
    '''
    t[0] = ('IF STATEMENT', ('CONDITION', t[2]), ('BODY', t[5]))


def p_13(t):
    '''
    loop        : R_WHILE  condition  COLON  LPAREN  program  RPAREN
    '''
    t[0] = ('WILE LOOP', ('CONDITION', t[2]), ('BODY', t[5]))


def p_14(t):
    '''
    condition   : BOOL
                | ID  condopt  value
                | LPAREN  condition  RPAREN
                | condition  condexpend  condition
    '''
    if len(t) == 4:
        if t[1] == '(':
            t[0] = (t[2])
        else:
            t[0] = (t[2], t[1], t[3])
    else:
        t[0] =  t[1]


def p_15(t):
    '''
    condopt     : EQUAL
                | NOTEQUAL
    '''
    t[0] = t[1]


def p_16(t):
    '''
    condexpend  : R_AND
                | R_NOT
                | R_OR
    '''
    t[0] = t[1]


def p_error(t):
    if t:
        print("Syntax error at: %s" % t.value)
    else:
        print("Syntax error .. God only knows where or why!")

parser = yacc.yacc()



# source_code = """
# def func(a, b, c, d):
#     (
#     if true:
#         ( x = 14 )
#     y = 500
#     )
# """
#
# parser.parse(source_code)

while True:
    parser.parse(input(">>> "))
