import re
from lexical_analyzer import *

t_keywords = Token({"Reserved Words": r'|'.join(['int', 'float'])})

t_int = Token({"Digits": r'[0-9]+'})

t_float = Token({"Sign": r'[-+]?',
                "Intgers" : t_int,
                "FloatingPoint" : r'\.',
                "decimals" : t_int,
                })

x = LaxicalAnalyzer({
            "Keyword"   : t_keywords,
            "Intger"    : t_int,
            "Float"     : t_float})

x.analyze(input())




# var_types = ['int', 'float', 'double', 'long', 'char', 'short', 'string']
# cmp_types = ['if', 'else', 'elif', 'while', 'for', 'try', 'except']
#
# token_key = re.compile(r'|'.join(var_types + cmp_types))
#
# token_int = re.compile(r'[0-9]+')
# token_var = re.compile(r'[_a-zA-Z]+[_a-zA-Z0-9]*')
#
#
# string = input()
#
# matchs = re.finditer(token_var, string)
#
#
# for value in matchs:
#     print(value)
