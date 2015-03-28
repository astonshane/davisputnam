import urllib2
import sys
from sets import Set
from literal import Literal

def parsedInput(given):
    url = "http://api.wolframalpha.com/v1/query?input=CNF+%s&appid=2Y4TEV-W2AETK4T5K&includepodid=Input" %  given
    req = urllib2.Request(url)
    response = urllib2.urlopen(req)
    the_page = response.read()
    the_page = the_page.split("\n")
    for line in the_page:
        line = line.lstrip()
        line = line.split(">")
        #print line
        if line[0] == "<plaintext":
            line = line[1].split("<")
            parsed = line[0]
    return parsed

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


'''
def Satisfiable(s):
    if S = {}:
        return true
    if S = {{}}:
        return false

    if {} in S:
        return false

    if {L} in S:
        return Satisfiable(S_L)

    select L in lit(s)
        return Satisfiable(S_L) | Satisfiable(S_L')
'''


if __name__ == "__main__":
    argv = sys.argv
    if len(argv) != 2:
        print "invalid useage"
        exit(1)

    infile = open(argv[1])
    lines = []
    for line in infile:
        line = line.strip("\n")
        line = line.replace(" ", "+")
        lines.append(line)

    S = [] #clause Set

    lines[-1] = "NOT(%s)" % lines[-1]
    for line in lines:
        #print line
        parsed = parsedInput(line)
        #print parsed
        newClauses = createClauses(parsed)
        #print newClauses
        for c in newClauses:
            S.append(c)

        #print ""

    print S
    #TODO: remove duplicates from S


    #print parsedInput("(P+and+Q)+or+(F+implies+G)")
