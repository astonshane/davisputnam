import urllib2
import sys

def parsedInput(given):
    url = "http://api.wolframalpha.com/v1/query?input=CNF+%s&appid=2Y4TEV-W2AETK4T5K" %  given
    #print url
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
        print line
        parsed = parsedInput(line)
        print parsed
