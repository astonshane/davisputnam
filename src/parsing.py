import urllib2
import sys
import threading
from sets import Set
from literal import Literal
from helpers import *
from cscreator import csCreator
from regex import *
from sanatize import *

#performs the http request to wolframalpha to convert the user's input to CNF
def parsedInput(given):
    #sample wolfram request:
    #http://api.wolframalpha.com/v1/query?input=BooleanConvert[(B+xnor+Z)+implies+not+Z,+%22CNF%22]&appid=2Y4TEV-W2AETK4T5K
    given = sanatize(given)
    #construct the url
    url = "http://api.wolframalpha.com/v1/query?input=BooleanConvert[" + given +",%22CNF%22]&appid=2Y4TEV-W2AETK4T5K"

    #make the request
    req = urllib2.Request(url)
    response = urllib2.urlopen(req)

    #parse the response
    the_page = response.read()
    the_page = the_page.split("\n")
    parsed = ""
    found = False
    for line in the_page:
        line = line.lstrip()
        line = line.split(">")

        #search for the SECOND line in the XML response that begins with <plaintext>
        #       This is the line that will contain our desired response
        if line[0] == "<plaintext":
            if found:
                #we got it!
                line = line[1].split("<")
                parsed = line[0]
                return parsed
            else:
                #we found the first line starting with <plaintext>
                found = True

#takes in a CNF representation of the user input and returns a set of clauses
#   that equivillently represent it
def createClauses(line):
    clauses = []
    #first split on "AND"
    line = line.split("AND")
    for clause in line:
        clause = clause.strip()
        #then split on OR
        clause = clause.split("OR")

        clause2 = []
        for l in clause:
            l = l.strip()
            #remvoe any parenthesies that may be left
            l = l.replace("(", "")
            l = l.replace(")", "")

            #split on spaces now
            l = l.split(" ")

            #create the desired literal (negated if the first element is now a NOT)
            if l[0] == "NOT":
                l = Literal(l[1], True)
            else:
                l = Literal(l[0], False)

            clause2.append(l)

        #add this new clause to the clauses that have been created thusfar
        clauses.append(clause2)

    return clauses


def worker(S, line):

    #makes the wolframalpha request and returns the CNF
    parsed = parsedInput(line)

    #check if this was determined to be a tautology
    #   if it was, this statement does not need to be added to the clausSet as it is
    #       trivially true
    if parsed == "True":
        print "    Tautology detected: not adding %s to S" % line.replace("+", " ")
        return

    #create new clauses from the CNF form of the given input line
    newClauses = createClauses(parsed)

    #add any new clauses to the clauseSet
    for c in newClauses:
        S.append(c)
    return


#reads in the argument from the provided file and returns a clauseSet representing it
def constructClauseSet(file):
    #open the file
    infile = open(file)

    lines = []
    #read in each line of the file (replacing special characters/words)
    for line in infile:
        line = prettify(line)
        lines.append(line)

    #clause set creator: (used in the multithreading bellow)
    cs_creator = csCreator()

    #negate the conclusion (which we define to be the last line in the input)
    print "negating the conclusion..."
    print "    %s" % lines[-1].replace("+", " ")
    lines[-1] = "NOT(%s)" % lines[-1]
    print "    %s" % lines[-1].replace("+", " ")

    #create a new thread for each line of the input
    #   each thread will create a wolframalpha request to convert it to CNF
    #       and the resulting clauses to the cs_creator object created above
    for line in lines:
        print "converting %s..." % line.replace("+", " ")
        if not tryRegex(line, cs_creator):
            t = threading.Thread(target=worker, args=(cs_creator, line, ))
            t.start()

    main_thread = threading.currentThread()
    for t in threading.enumerate():
        #join all of the previously created threads
        if t is not main_thread:
            t.join()

    #get the resulting clauseSet
    S = cs_creator.value

    return S
