import ply.lex as lex
import ply.yacc as yacc

reserved_types = {
        'int'       :'TYPE_INT',
        'bool'      :'TYPE_BOOL',
        'float'     :'TYPE_FLOAT',
        'string'    :'TYPE_STRING',


        'if'        :'R_IF',
        'for'       :'R_FOR',
        'while'     :'R_WHILE',
    }

tokens = [
    # Identifiers
    'ID',
    # Primitive data types
    'INTEGER', 'FLOAT', 'STRING', 'BOOL',
    # Literals
     "LPAREN", "RPAREN", "LBRACE", "RBRACE", "COLON", "COMMA", "DOT", "SEMICOLON", "NEWLINE",
    # Operators
     "PLUS", "MINUS", "MULTIPLY", "DIVIDE", "MOD", "ASSIGN", "EQUAL", "NOTEQUAL",
     ] + list(reserved_types.values())

# Token
t_FLOAT        = r'[+-]?' + r'\d+.\d+'
t_INTEGER      = r'[+-]?' + r'\d+'
t_STRING       = r'".*"'
t_BOOL         = r'(true)|(false)'
t_LPAREN       = r'\('
t_RPAREN       = r'\)'
t_LBRACE       = r'\{'
t_RBRACE       = r'\}'
t_COLON        = r'\:'
t_COMMA        = r'\,'
t_DOT          = r'\.'
t_SEMICOLON    = r'\;'
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

def t_error(t):
    print("Lexical error at the word: %s" % t.value[0])
    quit()

# Build the lexer
lexer = lex.lex()


var_table = {}

# Parsing rules
def p_validline(t):
    '''
    validline   : assignment
                | statement
                | loop
                | NEWLINE
    '''

def p_statement(t):
    '''
    statement   : ID  ASSIGN  ID
                | ID  ASSIGN  BOOL
                | ID  ASSIGN  FLOAT
                | ID  ASSIGN  STRING
                | ID  ASSIGN  INTEGER
    '''
    if t[1] in var_table:
        if var_table[t[1]] != t[3]:
            print("Syntax error: cant assigen %s to %s" % (t[3], var_table[t[1]]))

    else:
        print("Syntax error: %s must be declared before assigned value" % t[1])

def p_assignment(t):
    '''
    assignment  : TYPE_INT      ID  ASSIGN  INTEGER

                | TYPE_FLOAT    ID  ASSIGN  FLOAT
                | TYPE_FLOAT    ID  ASSIGN  INTEGER

                | TYPE_STRING   ID  ASSIGN  STRING
    '''
    var_table[t[2]] = t[1]
    print(type(t[1]))

def p_loop(t):
    '''
    loop        : R_IF      condition   COLON
                | R_WHILE   condition   COLON
    '''

def p_condition(t):
    '''
    condition       : ID    condition_op    value
                    | BOOL

    condition_op    : EQUAL
                    | NOTEQUAL

    value           : ID
                    | INTEGER
                    | FLOAT
                    | STRING
                    | BOOL
    '''

def p_error(t):
    print("Syntax error at the word: %s" % t.value)

parser = yacc.yacc()

while True:
    parser.parse(input())
