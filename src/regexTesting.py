import re

line = "A and B"

m = re.match('(\w) AND (\w)$', line, re.I)

if m:
    print m.group(1), m.group(2)
else:
    print "nope"
