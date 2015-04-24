import re

line = "A k"

m = re.match('(\w)$', line, re.I)

if m:
    print m.group(1)
else:
    print "nope"
