import re
from literal import *
from cscreator import *

#try to match the line with the implication pattern
def implies(line):
    #######################################################
    #       ~A -> ~B
    m = re.match('NOT (\w+) implies NOT (\w+)$', line, re.I)
    if m:
        clause = []

        #CNF: A v ~B

        clause.append(Literal(m.group(1), False))
        clause.append(Literal(m.group(2), True))

        return clause

    #######################################################
    #       ~A -> B
    m = re.match('NOT (\w+) implies (\w+)$', line, re.I)
    if m:
        clause = []

        #CNF: A v B

        clause.append(Literal(m.group(1), False))
        clause.append(Literal(m.group(2), False))

        return clause

    #######################################################
    #       A -> ~B
    m = re.match('(\w+) implies NOT (\w+)$', line, re.I)
    if m:
        clause = []

        #CNF: ~A v ~B

        clause.append(Literal(m.group(1), True))
        clause.append(Literal(m.group(2), True))

        return clause

    #######################################################
    #       A -> B
    m = re.match('(\w+) implies (\w+)$', line, re.I)
    if m:
        clause = []

        #CNF: ~A v B

        clause.append(Literal(m.group(1), True))
        clause.append(Literal(m.group(2), False))

        return clause

def iff(line):
    clauses = []
    #######################################################
    #       ~A <-> ~B
    m = re.match('NOT (\w+) xnor NOT (\w+)$', line, re.I)
    if m:

        #CNF: (A v ~B) and (B or ~A)

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
    #       ~A <-> B
    m = re.match('NOT (\w+) xnor (\w+)$', line, re.I)
    if m:

        #CNF: (~A v ~B) and (A or B)

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
    #       A <-> ~B
    m = re.match('(\w+) xnor NOT (\w+)$', line, re.I)
    if m:

        #CNF: (~A v ~B) and (A or B)

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
    #       A <-> B
    m = re.match('(\w+) xnor (\w+)$', line, re.I)
    if m:

        #CNF: (A v ~B) and (B or ~A)

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
    #######################################################
    #       A
    m = re.match('(\w)$', line, re.I)
    if m:
        l = Literal(m.group(1), False)
        return [l]

    #######################################################
    #       ~A
    m = re.match('NOT (\w)$', line, re.I)
    if m:
        l = Literal(m.group(1), True)
        return [l]

def conjunction(line):
    clauses = []

    #######################################################
    #       A ^ B
    m = re.match('(\w) and (\w)$', line, re.I)
    if m:
        l = Literal(m.group(1), False)
        k = Literal(m.group(2), False)

        clauses.append([l])
        clauses.append([k])

        return clauses

    #######################################################
    #       ~A ^ B
    m = re.match('not (\w) and (\w)$', line, re.I)
    if m:
        l = Literal(m.group(1), True)
        k = Literal(m.group(2), False)

        clauses.append([l])
        clauses.append([k])

        return clauses

    #######################################################
    #       A ^ ~B
    m = re.match('(\w) and not (\w)$', line, re.I)
    if m:
        l = Literal(m.group(1), False)
        k = Literal(m.group(2), True)

        clauses.append([l])
        clauses.append([k])

        return clauses

    #######################################################
    #       ~A ^ ~B
    m = re.match('not (\w) and not (\w)$', line, re.I)
    if m:
        l = Literal(m.group(1), True)
        k = Literal(m.group(2), True)

        clauses.append([l])
        clauses.append([k])

        return clauses

def disjunction(line):
    #######################################################
    #       A v B
    m = re.match('(\w) or (\w)$', line, re.I)
    if m:
        l = Literal(m.group(1), False)
        k = Literal(m.group(2), False)

        clause = []
        clause.append(l)
        clause.append(k)
        return clause

    #######################################################
    #       ~A v B
    m = re.match('not (\w) or (\w)$', line, re.I)
    if m:
        l = Literal(m.group(1), True)
        k = Literal(m.group(2), False)

        clause = []
        clause.append(l)
        clause.append(k)
        return clause

    #######################################################
    #       A v ~B
    m = re.match('(\w) or not (\w)$', line, re.I)
    if m:
        l = Literal(m.group(1), False)
        k = Literal(m.group(2), True)

        clause = []
        clause.append(l)
        clause.append(k)
        return clause

    #######################################################
    #       ~A v ~B
    m = re.match('not (\w) or not (\w)$', line, re.I)
    if m:
        l = Literal(m.group(1), True)
        k = Literal(m.group(2), True)

        clause = []
        clause.append(l)
        clause.append(k)
        return clause

#attempts to match the given line to a pattern which we already know the
#   CNF for and is relatively simple to parse in order to avoid the
#   costly wolfram API calls that take forever
def tryRegex(line, cs_creator):
    line = line.replace("+", " ")

    #try to match the line against any literals (e.g. A,  ~A)
    m = lit(line)
    if m:
        cs_creator.append(m)

    #try to match the line with the implication pattern (e.g. A -> B)
    m = implies(line)
    if m:
        cs_creator.append(m)
        return True

    #try to match the line with the iff pattern (e.g. A <-> B)
    m = iff(line)
    if m:
        for n in m:
            cs_creator.append(n)
        return True

    #try to match the line with the and pattern (e.g. A ^ B)
    m = conjunction(line)
    if m:
        for n in m:
            cs_creator.append(n)
        return True

    #try to match the line with the or pattern (e.g. A v B)
    m = disjunction(line)
    if m:
        cs_creator.append(m)
        return True

    #we didn't find any matches, return false
    return False

'''
m = tryRegex(line = "A implies not Q")
if m:
    print "banana"
'''
