from scanner import Scanner
from naive_parser import Parser

lx = Scanner()
lx.set_source_code(open('Z+Source.txt', 'r').read())

pg = Parser()
