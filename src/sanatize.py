#read in each line of the file (replacing special characters/words)
#   puts the line in a form that can more easily be parsed / given to wolfram
def sanatize(line):
    line = line.strip("\n")
    line = line.replace(" ", "+")
    line = line.replace("iff", "xnor")
    line = line.replace("IFF", "xnor")

    line = line.replace("~", "NOT+")
    line = line.replace("^", "and")
    line = line.replace("v", "or")
    line = line.replace("<->", "xnor")
    line = line.replace("->", "implies")

    return line

#take any inputs and make them into a "pretty" format
#           NOT A        ==     ~A
#           A AND B      ==     A ^ B
#           A OR B       ==     A v B
#           A implies B  ==     A -> B
#           A iff B      ==     A <-> B
def prettify(line):
    line = line.strip("\n")

    line = line.replace("NOT ", "~")
    line = line.replace("NOT", "~")
    line = line.replace("not ", "~")
    line = line.replace("not", "~")

    line = line.replace("AND", "^")
    line = line.replace("and", "^")

    line = line.replace("OR", "v")
    line = line.replace("or", "v")

    line = line.replace("iff", "<->")
    line = line.replace("IFF", "<->")
    line = line.replace("xnor", "<->")
    line = line.replace("XNOR", "<->")

    line = line.replace("implies", "->")
    line = line.replace("IMPLIES", "->")
    
    return line
