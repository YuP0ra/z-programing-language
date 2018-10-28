import re
from lexical_analyzer import *

t_keywords = r'|'.join(['int', 'float'])

t_int = r'[0-9]+'
t_float = r'[-+]?' + t_int + r'\.' + t_int

t_var = r'[_a-zA-Z]+[_a-zA-Z0-9]*'
t_opr = r'[-+/*=<>]=?'

x = LaxicalAnalyzer({
            "Keyword"   : t_keywords,
            "Variable"  : t_var,
            "Intger"    : t_int,
            "Float"     : t_float,
            "Operator"  : t_opr})

x.analyze(input())
