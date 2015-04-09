from sets import Set
from literal import Literal

def clauseEq(c1, c2):
    if len(c1) == len(c2):
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

def literalInClauseSet(lit, S):
    for clause in S:
        if literalInClause(lit, clause):
            return True
    return False

def nextLiteral(S):
    clause = S[0][0]
    return clause.name

def literalInClause(l1, C):
    for l in C:
        if l == l1:
            return True
    return False

#subsumption:
#   [A,B] subsumes [A,B,C]
def subsume(clause1, clause2):
    for lit in clause1:
        if not literalInClause(lit, clause2):
            return False
    return True

def findPureLiteral(S):
    for clause in S:
        for lit in clause:
            notlit = Literal(lit.name, not lit.negated)
            if not literalInClauseSet(notlit, S):
                return lit
    return None
