import ply.lex as lex
import ply.yacc as yacc

reserved_types = {
        'def'       :'R_DEF',
    }

tokens = [
    # Identifiers
    'ID',
    # Primitive data types
    'NUM',
    # Literals
     "LPAREN", "RPAREN", "NEWLINE",
    # Operators
     "PLUS", "MINUS", "MULTIPLY", "DIVIDE", "MOD", "ASSIGN",
     ] + list(reserved_types.values())

# Token
t_NUM          = r'[+-]?\d+'
t_LPAREN       = r'\('
t_RPAREN       = r'\)'
t_MULTIPLY     = r'\*'
t_DIVIDE       = r'\/'
t_PLUS         = r'\+'
t_MINUS        = r'\-'
t_MOD          = r'%'
t_ASSIGN       = r'='

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


def p_0(t):
    '''
    sourcecode  : NEWLINE
                | varcall
                | assignment
                |
    '''

def p_1(t):
    '''
    assignment  : ID ASSIGN expression
    '''
    try:
        var_table[t[1]] = int(t[3])
    except Exception as e:
        print("Error! Reading undefiend variable")


def p_2(t):
    '''
    varcall     : ID
    '''
    if t[1] in var_table:
        print(var_table[t[1]])
    else:
        print("Error! Reading undefiend variable")


def p_3(t):
    '''
    expression  : LPAREN        expression  RPAREN
                | expression    MOD         expression
                | expression    PLUS        expression
                | expression    MINUS       expression
                | expression    DIVIDE      expression
                | expression    MULTIPLY    expression
                | NUM
                | ID
    '''

    if len(t) == 2:
        if t[1] in var_table:
            t[0] = var_table[t[1]]
        else:
            t[0] = int(t[1])


    if len(t) == 4:
        if t[2] == '+':
            t[0] = t[1] + t[3]

        if t[2] == '-':
            t[0] = t[1] - t[3]

        if t[2] == '*':
            t[0] = t[1] * t[3]

        if t[2] == '/':
            t[0] = t[1] / t[3]

        if t[2] == '%':
            t[0] = t[1] % t[3]

        if t[1] == '(':
            t[0] = t[2]


def p_error(t):
    if t:
        print("Syntax error at the word: %s" % t)
    else:
        print("Syntax error .. God only knows where or why!")

parser = yacc.yacc()

while True:
    parser.parse(input(">>> "))
