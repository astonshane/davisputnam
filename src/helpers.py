from sets import Set
from literal import Literal

#determines if two clauses are equal
def clauseEq(c1, c2):
    #each clause must have the same number of elements
    if len(c1) == len(c2):
        for i in range(0, len(c1)):
            #check each element and make sure they match
            if c1[i] != c2[i]:
                return False
        return True
    else:
        return False

#determines if a clause is in the given clauseSet S
def clauseIn(c1, S):
    found = False
    for c in S:
        if clauseEq(c1, c):
            return True
    return False

#determines if a given literal is in the given clausSet S
def literalInClauseSet(lit, S):
    for clause in S:
        #checks to see if the literal is in any of the cluases in S
        if literalInClause(lit, clause):
            return True
    return False

#determines if a literal is in a clause
def literalInClause(l1, C):
    for l in C:
        if l == l1:
            return True
    return False

#determines the name of the first literal in S
#ex: if S = [[~B,C], [A,B,C]]
#     nextLiteral(S) returns B
def nextLiteral(S):
    #returns the first element of the first clause in S
    #assumes that the first element is a list of at least size 1
    #       which should be gaurenteed by the checks performed in satisfiable()
    clause = S[0][0]
    return clause.name


#subsumption:
#   [A,B] subsumes [A,B,C]
#   subsume() determines if c1 subsumes c2
def subsume(clause1, clause2):
    for lit in clause1:
        #check that each literal in c1 is also in c2
        if not literalInClause(lit, clause2):
            return False
    return True

#pure literals:
#   a literal L is pure with regard to a clause set S if and only if
#      L is contained in at least one clause in S, but ~L is not
#   findPureLiteral(S) returns the first literal, if any, that is pure from S
def findPureLiteral(S):
    for clause in S:
        for lit in clause:
            notlit = Literal(lit.name, not lit.negated)
            if not literalInClauseSet(notlit, S):
                return lit
    return None
