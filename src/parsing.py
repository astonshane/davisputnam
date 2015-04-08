import urllib2
import sys
from sets import Set
from literal import Literal
from helpers import *

def parsedInput(given):
    #http://api.wolframalpha.com/v1/query?input=BooleanConvert[(B+xnor+Z)+implies+not+Z,+%22CNF%22]&appid=2Y4TEV-W2AETK4T5K
    url = "http://api.wolframalpha.com/v1/query?input=BooleanConvert[" + given +",%22CNF%22]&appid=2Y4TEV-W2AETK4T5K"

    req = urllib2.Request(url)
    response = urllib2.urlopen(req)
    the_page = response.read()
    the_page = the_page.split("\n")
    parsed = ""
    found = False
    for line in the_page:
        line = line.lstrip()
        line = line.split(">")
        #print line
        if line[0] == "<plaintext":
            #print line
            if found:
                line = line[1].split("<")
                parsed = line[0]
                return parsed
            else:
                found = True


def createClauses(line):
    clauses = []
    line = line.split("AND")
    for clause in line:
        clause = clause.strip()
        clause = clause.split("OR")

        clause2 = []
        for l in clause:
            l = l.strip()
            l = l.replace("(", "")
            l = l.replace(")", "")

            l = l.split(" ")
            if l[0] == "NOT":
                l = Literal(l[1], True)
            else:
                l = Literal(l[0], False)

            clause2.append(l)


        clauses.append(clause2)

    return clauses


def constructClauseSet(file):
    infile = open(file)
    lines = []
    for line in infile:
        line = line.strip("\n")
        line = line.replace(" ", "+")
        line = line.replace("iff", "xnor")
        line = line.replace("IFF", "xnor")
        lines.append(line)

    S = [] #clause Set

    print "negating the conclusion..."
    print "    %s" % lines[-1].replace("+", " ")
    lines[-1] = "NOT(%s)" % lines[-1]
    print "    %s" % lines[-1].replace("+", " ")

    for line in lines:
        print "converting %s..." % line.replace("+", " ")
        parsed = parsedInput(line)
        print "    CNF: %s" % parsed
        newClauses = createClauses(parsed)
        print "    Clauses:", newClauses
        for c in newClauses:
            if not clauseIn(c, S):
                S.append(c)

    return S
