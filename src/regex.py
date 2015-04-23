import re
from literal import *

def implies(line):
    #######################################################
    m = re.match('NOT (\w+) implies NOT (\w+)', line, re.I)
    if m:
        clause = []

        clause.append(Literal(m.group(1), False))
        clause.append(Literal(m.group(2), True))

        return clause

    #######################################################
    m = re.match('NOT (\w+) implies (\w+)', line, re.I)
    if m:
        clause = []

        clause.append(Literal(m.group(1), False))
        clause.append(Literal(m.group(2), False))

        return clause

    #######################################################
    m = re.match('(\w+) implies NOT (\w+)', line, re.I)
    if m:
        clause = []

        clause.append(Literal(m.group(1), True))
        clause.append(Literal(m.group(2), True))

        return clause

    #######################################################
    m = re.match('(\w+) implies (\w+)', line, re.I)
    if m:
        clause = []

        clause.append(Literal(m.group(1), True))
        clause.append(Literal(m.group(2), False))

        return clause



def tryRegex(line):
    m = implies(line)
    if m:
        print m


m = tryRegex(line = "A implies not Q")
if m:
    print "banana"
