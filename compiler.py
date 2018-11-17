
from scanner import Scanner

lx = Scanner()
lx.set_source_code(input())

for value in lx.next():
    print(value)
