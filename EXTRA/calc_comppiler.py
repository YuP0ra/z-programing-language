import ply.lex as lex
import ply.yacc as yacc

tokens = [
    # Identifiers
    'ID',
    # Primitive data types
    'NUM',
    # Literals
     "LPAREN", "RPAREN", "NEWLINE",
    # Operators
     "PLUS", "MINUS", "MULTIPLY", "DIVIDE", "POW", "MOD", "ASSIGN",
     ]

# Token
t_NUM          = r'[+-]?\d+(.\d+)?'
t_LPAREN       = r'\('
t_RPAREN       = r'\)'
t_MULTIPLY     = r'\*'
t_DIVIDE       = r'\/'
t_PLUS         = r'\+'
t_MINUS        = r'\-'
t_MOD          = r'%'
t_POW          = r'\*\*'
t_ASSIGN       = r'='

# Ignored characters
t_ignore = " \t"

def t_ID(t):
    r'[_a-zA-Z]+[_a-zA-Z0-9]*'
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
    ('left', 'POW'),
)


def p_0(t):
    '''
    sourcecode  : NEWLINE
                | varcall
                | assignment
                | pure_expression
    '''

def p_1(t):
    '''
    varcall     : ID
    '''
    if t[1] in var_table:
        print(var_table[t[1]])
    else:
        print("Error! Reading undefiend variable")


def p_2(t):
    '''
    assignment  : ID ASSIGN expression
    '''
    try:
        var_table[t[1]] = float(t[3])
    except Exception as e:
        print("Error! Reading undefiend variable")

def p_3(t):
    '''
    pure_expression  : expression
    '''
    try:
        print(t[1])
    except Exception as e:
        print("Error! Reading undefiend variable")


def p_4(t):
    '''
    expression  : LPAREN        expression  RPAREN
                | expression    MOD         expression
                | expression    POW         expression
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
            t[0] = float(t[1])


    if len(t) == 4:
        if t[2] == '+':
            t[0] = t[1] + t[3]

        if t[2] == '-':
            t[0] = t[1] - t[3]

        if t[2] == '*':
            t[0] = t[1] * t[3]

        if t[2] == '**':
            t[0] = t[1] ** t[3]

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
