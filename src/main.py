import urllib2
import sys
from sets import Set

#my helper functions / classes
from literal import Literal
from helpers import *
from parsing import *

#reduction function that transforms S
#   by removing any clauses that contain the literal L1
#   and removing L2 (i.e. ~L1) from any clauses that contain it
def reduce(L1, L2, S):
    newS = []
    for c in S:
        '''
        if L1 in c:
           this clause is true now
           don't add c it to newS
       else if L2 (i.e. ~L1) in c:
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
#main recursive function for determining whether or not a given clauseset is satisfiable
#   using the algorithm described above, with additional improvements as seen fit
def satisfiable(S, i, subsumption, pureLiteral, unitLiteral):
    #sort the clause Set by the size of each clause
    S.sort(lambda x,y: cmp(len(x), len(y)))
    print ""
    print " "*i +  "Satisfiable() for Clause Set: ", S


    #if S = []: return True
    if len(S) == 0:
        print " "*i +  "    S == []; returning True"
        return True

    #if [] in S: return False
    #if [] in S:
    #    return False
    firstElement = next(iter(S))
    if firstElement == []:
        print " "*i +  "    Found [] in S. Returning False"
        return False

    #tautological elimination
    #   done by wolfram automatically during conversion to CNF
    #   see worker() in parsing.py

    #subsumption elimination:
    #   [A,B] subsumes [A,B,C]
    #   Hence, with S any clause set, and S1 the clause set
    #        S with all subsumed clauses removed: S is
    #        satisfiable if and only if S1 is satisfiable.
    if subsumption:
        for clause1 in S:
            newS = []
            for clause2 in S:
                if clauseEq(clause1, clause2):
                    newS.append(clause1)
                    continue

                if not subsume(clause1, clause2):
                    newS.append(clause2)
                else:
                    print " " * (i+4) + "%s subsumes %s" % (str(clause1), str(clause2))

            if len(newS) != len(S):
                return satisfiable(newS, i+4, subsumption, pureLiteral, unitLiteral)


    #pure literal elimination:
    #   a literal L is pure with regard to a clause set S if and only if
    #      L is contained in at least one clause in S, but ~L is not
    #   a clause is pure with regard to a clause set S, iff it contains
    #       a pure literal
    #   obviously, with S, any clause set, and with S1 the clause set S
    #       with all pure clauses removed: S is satisfiable iff S' is satisfiable
    if pureLiteral:
        pl = findPureLiteral(S)
        if pl != None:
            print " "*i + "    %s found to be a pure literal" % str(pl)
            newS = []
            for clause in S:
                if not literalInClause(pl, clause):
                    newS.append(clause)
            return satisfiable(newS, i + 4, subsumption, pureLiteral, unitLiteral)

    #unit rule:
    #   if {L} in S:
    #    return Satisfiable(S_L)
    if unitLiteral:
        #becuase we sort by size, the first element will always be the shortest
        #       (ie. if there is anything of size 1, it will be found in the first spot)
        if len(firstElement) == 1:
            print " "*i +  "    Exploiting Unit Rule with", firstElement[0]

            firstLiteral =  firstElement[0]
            notFirstLiteral = Literal(firstLiteral.name, not firstLiteral.negated)
            S1 = reduce(firstLiteral, notFirstLiteral, S)

            return satisfiable(S1, i + 4, subsumption, pureLiteral, unitLiteral)

    #find the next Literal that we will split on
    nextL = nextLiteral(S)

    print " "*i +  "    Branching on", nextL
    L1 = Literal(nextL, False)
    L2 = Literal(nextL, True)

    S1 = reduce(L1, L2, S)
    S2 = reduce(L2, L1, S)

    return satisfiable(S1, i + 4, subsumption, pureLiteral, unitLiteral) or satisfiable(S2, i + 4, subsumption, pureLiteral, unitLiteral)

if __name__ == "__main__":
    argv = sys.argv

    #add-on flags (set them initially to false)
    subsumption = False
    pureLiteral = False
    unitLiteral = False

    for i in range(2,len(argv)):
        #use ALL of the add-ons: subsumption, pureLiteral, and unitLiteral
        if argv[i] == "-a":
            subsumption = True
            pureLiteral = True
            unitLiteral = True

        #use subsumption
        elif argv[i] == "-s":
            subsumption = True

        #use pureLiteral
        elif argv[i] == "-p":
            pureLiteral = True

        #use unitLiteral
        elif argv[i] == "-u":
            unitLiteral = True

        #invalid useage:
        else:
            print "Useage: python main.py <input file> [-a] [-s] [-p] [-u]\n"
            print "-a        use all add-ons"
            print "-s        subsumption elimination"
            print "-p        pure literal elimination"
            print "-u        unit literal elimination"
            exit(1)

    print "Starting Satisfiable() with the following add-ons:"
    print "    Subsumption: ", subsumption
    print "    Pure Literal:", pureLiteral
    print "    Unit Literal:", unitLiteral

    S = constructClauseSet(argv[1])

    print "\nStarting Clause Set S: ", S

    #       setting any of the below to false will "turn off", that add-on
    #      sasisfiable(ClauseSet, startingIndent, subsumption, pureLiteral, unitLiteral)
    sat =  satisfiable(S, 0, subsumption, pureLiteral, unitLiteral)
    if sat:
        print "S was satisfiable! Therefore given argument is invalid!"
    else:
        print "S was not satisfiable! Therefore given argument is valid!"
