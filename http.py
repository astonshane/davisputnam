import urllib2

url = "http://api.wolframalpha.com/v1/query?input=CNF+(P+and+Q)+or+(F+implies+G)&appid=2Y4TEV-W2AETK4T5K&includepodid=Input"
req = urllib2.Request(url)
response = urllib2.urlopen(req)
the_page = response.read()
the_page = the_page.split("\n")
for line in the_page:
    line = line.lstrip()
    line = line.split(">")
    #print line
    if line[0] == "<plaintext":
        line = line[1].split("<")
        parsed = line[0]

print parsed
