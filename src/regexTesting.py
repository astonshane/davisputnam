import re

line = "NOT A implies NOT Q;"

m = re.match('NOT (\w) implies NOT (\w)', line, re.I)

if m:
    print m.group(1), m.group(2)
else:
    print "nope"
