import urllib2
import sys
from sets import Set
from literal import Literal

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


def clauseEq(c1, c2):
    if len(c) == len(c2):
        for i in range(0, len(c1)):
            if not(c1[i].name == c2[i].name and c1[i].negated == c2[i].negated):
                return False
        return True
    else:
        return False

def clauseIn(c1, S):
    found = False
    for c in S:
        if clauseEq(c1, c):
            return True
    return False

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

def nextLiteral(S):
    clause = S[0][0]
    return clause.name

def literalInClause(l1, C):
    for l in C:
        if l == l1:
            return True
    return False

def reduce(L1, L2, S):
    newS = []
    for c in S:
        '''
        if L1 in c:
           this clause is true now
           don't add c it to newS
        else if L2 (ie ~L1) in c:
           remove L2 from c
           add new c to newS
        else: (neither L1 nor L2 in c)
           add it to newS
        '''

        if literalInClause(L1, c):
            continue
        elif literalInClause(L2, c):
            newC = []
            for l in c:
                if l != L2:
                    newC.append(l)

            newS.append(newC)
        else:
            newS.append(c)

    return newS


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

def satisfiable(S, i=0):
    #sort the clause Set by the size of each clause
    S.sort(lambda x,y: cmp(len(x), len(y)))
    print " "*i, "satisfiable for Clause Set: ", S


    #if S = []: return True
    if len(S) == 0:
        print " "*i, "    S == []; returning True"
        return True

    #if [] in S: return False
    #if [] in S:
    #    return False
    firstElement = next(iter(S))
    if firstElement == []:
        print " "*i, "    Found [] in S. Returning False"
        return False


    #unit rule:
    #   if {L} in S:
    #    return Satisfiable(S_L)
    if len(firstElement) == 1:
        print " "*i, "    Exploiting Unit Rule with", firstElement[0]

        firstLiteral =  firstElement[0]
        notFirstLiteral = Literal(firstLiteral.name, not firstLiteral.negated)
        S1 = reduce(firstLiteral, notFirstLiteral, S)

        return satisfiable(S1, i+4)


    nextL = nextLiteral(S)
    #print nextL
    print " "*i, "    Branching on", nextL
    L1 = Literal(nextL, False)
    L2 = Literal(nextL, True)

    S1 = reduce(L1, L2, S)
    S2 = reduce(L2, L1, S)

    #print "  ",
    #print S1
    #print "  ",
    #print S2

    return satisfiable(S1, i+4) or satisfiable(S2, i+4)

    #return True


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
        line = line.replace("iff", "xnor")
        line = line.replace("IFF", "xnor")
        lines.append(line)

    S = [] #clause Set

    print "negating the conclusion... [%s" % lines[-1].replace("+", " "),
    lines[-1] = "NOT(%s)" % lines[-1]
    print " to %s]" % lines[-1].replace("+", " ")

    for line in lines:
        print "converting %s..." % line.replace("+", " ")
        parsed = parsedInput(line)
        print "    CNF: %s" % parsed
        newClauses = createClauses(parsed)
        print "    Clauses:", newClauses
        for c in newClauses:
            if not clauseIn(c, S):
                S.append(c)

        #print ""

    print "\nStarting Clause Set S: ", S
    sat =  satisfiable(S)
    if sat:
        print "S was satisfiable! Therefore given argument is invalid!"
    else:
        print "S was not satisfiable! Therefore given argument is valid!"
