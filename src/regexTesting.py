import re

line = "A XNOR B"

m = re.match('(\w) XNOR (\w)', line, re.I)

if m:
    print m.group(1), m.group(2)
else:
    print "nope"
