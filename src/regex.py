import re
from literal import *
from cscreator import *

def implies(line):
    #######################################################
    m = re.match('NOT (\w+) implies NOT (\w+)$', line, re.I)
    if m:
        clause = []

        clause.append(Literal(m.group(1), False))
        clause.append(Literal(m.group(2), True))

        return clause

    #######################################################
    m = re.match('NOT (\w+) implies (\w+)$', line, re.I)
    if m:
        clause = []

        clause.append(Literal(m.group(1), False))
        clause.append(Literal(m.group(2), False))

        return clause

    #######################################################
    m = re.match('(\w+) implies NOT (\w+)$', line, re.I)
    if m:
        clause = []

        clause.append(Literal(m.group(1), True))
        clause.append(Literal(m.group(2), True))

        return clause

    #######################################################
    m = re.match('(\w+) implies (\w+)$', line, re.I)
    if m:
        clause = []

        clause.append(Literal(m.group(1), True))
        clause.append(Literal(m.group(2), False))

        return clause

def iff(line):
    clauses = []
    #######################################################
    m = re.match('NOT (\w+) xnor NOT (\w+)$', line, re.I)
    if m:

        l = Literal(m.group(1), False)
        notl = Literal(m.group(1), True)

        k = Literal(m.group(2), False)
        notk = Literal(m.group(2), True)

        clause1 = []
        clause2 = []

        clause1.append(l)
        clause1.append(notk)

        clause2.append(k)
        clause2.append(notl)

        clauses.append(clause1)
        clauses.append(clause2)

        return clauses

    #######################################################
    m = re.match('NOT (\w+) xnor (\w+)$', line, re.I)
    if m:

        l = Literal(m.group(1), False)
        notl = Literal(m.group(1), True)

        k = Literal(m.group(2), False)
        notk = Literal(m.group(2), True)

        clause1 = []
        clause2 = []

        clause1.append(l)
        clause1.append(k)

        clause2.append(notl)
        clause2.append(notk)

        clauses.append(clause1)
        clauses.append(clause2)

        return clauses
    #######################################################
    m = re.match('(\w+) xnor NOT (\w+)$', line, re.I)
    if m:

        l = Literal(m.group(1), False)
        notl = Literal(m.group(1), True)

        k = Literal(m.group(2), False)
        notk = Literal(m.group(2), True)

        clause1 = []
        clause2 = []

        clause1.append(l)
        clause1.append(k)

        clause2.append(notl)
        clause2.append(notk)

        clauses.append(clause1)
        clauses.append(clause2)

        return clauses
    #######################################################
    m = re.match('(\w+) xnor (\w+)$', line, re.I)
    if m:

        l = Literal(m.group(1), False)
        notl = Literal(m.group(1), True)

        k = Literal(m.group(2), False)
        notk = Literal(m.group(2), True)

        clause1 = []
        clause2 = []

        clause1.append(l)
        clause1.append(notk)

        clause2.append(k)
        clause2.append(notl)

        clauses.append(clause1)
        clauses.append(clause2)

        return clauses

def lit(line):
    m = re.match('(\w)$', line, re.I)
    if m:
        l = Literal(m.group(1), False)
        return [l]

    m = re.match('NOT (\w)$', line, re.I)
    if m:
        l = Literal(m.group(1), True)
        return [l]

def conjunction(line):
    clauses = []

    m = re.match('(\w) and (\w)$', line, re.I)
    if m:
        l = Literal(m.group(1), False)
        k = Literal(m.group(2), False)

        clauses.append([l])
        clauses.append([k])

        return clauses

    m = re.match('not (\w) and (\w)$', line, re.I)
    if m:
        l = Literal(m.group(1), True)
        k = Literal(m.group(2), False)

        clauses.append([l])
        clauses.append([k])

        return clauses

    m = re.match('(\w) and not (\w)$', line, re.I)
    if m:
        l = Literal(m.group(1), False)
        k = Literal(m.group(2), True)

        clauses.append([l])
        clauses.append([k])

        return clauses

    m = re.match('not (\w) and not (\w)$', line, re.I)
    if m:
        l = Literal(m.group(1), True)
        k = Literal(m.group(2), True)

        clauses.append([l])
        clauses.append([k])

        return clauses

def disjunction(line):
    m = re.match('(\w) or (\w)$', line, re.I)
    if m:
        l = Literal(m.group(1), False)
        k = Literal(m.group(2), False)

        clause = []
        clause.append(l)
        clause.append(k)
        return clause

    m = re.match('not (\w) or (\w)$', line, re.I)
    if m:
        l = Literal(m.group(1), True)
        k = Literal(m.group(2), False)

        clause = []
        clause.append(l)
        clause.append(k)
        return clause

    m = re.match('(\w) or not (\w)$', line, re.I)
    if m:
        l = Literal(m.group(1), False)
        k = Literal(m.group(2), True)

        clause = []
        clause.append(l)
        clause.append(k)
        return clause

    m = re.match('not (\w) or not (\w)$', line, re.I)
    if m:
        l = Literal(m.group(1), True)
        k = Literal(m.group(2), True)

        clause = []
        clause.append(l)
        clause.append(k)
        return clause


def tryRegex(line, cs_creator):
    line = line.replace("+", " ")

    m = lit(line)
    if m:
        cs_creator.append(m)

    m = implies(line)
    if m:
        cs_creator.append(m)
        return True

    m = iff(line)
    if m:
        for n in m:
            cs_creator.append(n)
        return True

    m = conjunction(line)
    if m:
        for n in m:
            cs_creator.append(n)
        return True

    m = disjunction(line)
    if m:
        cs_creator.append(m)
        return True

    return False

'''
m = tryRegex(line = "A implies not Q")
if m:
    print "banana"
'''
