import urllib2
import sys
from sets import Set
from literal import Literal

def parsedInput(given):
        #http://api.wolframalpha.com/v1/query?input=BooleanConvert[(B+xnor+Z)+implies+not+Z,+%22CNF%22]&appid=2Y4TEV-W2AETK4T5K

    url = "http://api.wolframalpha.com/v1/query?input=BooleanConvert[" + given +",%22CNF%22]&appid=2Y4TEV-W2AETK4T5K"
    #url = "http://api.wolframalpha.com/v1/query?input=CNF+%s&appid=2Y4TEV-W2AETK4T5K" %  given
    print url
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
    #print "reducing on ",
    #print  L1,
    #print S
    newS = []
    for c in S:
        #if L1 in c:
        #   this clause is true now
        #       don't add c it to newS
        #else if L2 in c:
        #   remove L2 from c
        #   add new c to newS

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

    #print "reduced to ",
    #print newS
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

def satisfiable(S):
    #sort the clause Set by the size of each clause
    S.sort(lambda x,y: cmp(len(x), len(y)))
    #print S
    #if S = []: return True
    if len(S) == 0:
        #print "True"
        return True

    #if [] in S: return False
    #if [] in S:
    #    return False

    for s in S:
        if s == []:
            return False

    nextL = nextLiteral(S)
    #print nextL
    L1 = Literal(nextL, False)
    L2 = Literal(nextL, True)

    S1 = reduce(L1, L2, S)
    S2 = reduce(L2, L1, S)

    #print "  ",
    #print S1
    #print "  ",
    #print S2

    return satisfiable(S1) or satisfiable(S2)

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

    lines[-1] = "NOT(%s)" % lines[-1]
    for line in lines:
        print line
        parsed = parsedInput(line)
        print parsed
        newClauses = createClauses(parsed)
        #print newClauses
        for c in newClauses:
            if not clauseIn(c, S):
                S.append(c)

        #print ""

    print S
    sat =  satisfiable(S)
    if sat:
        print "S was satisfiable! Therefore given argument is invalid!"
    else:
        print "S was not satisfiable! Therefore given argument is valid!"
