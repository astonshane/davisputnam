# Dependencies
 - Python 2.7.* (developed with 2.7.6)

# Runtime Instructions

 - python main.py  &lt;input file&gt; [-a] [-s] [-u]
  - -a        use all add-ons
  - -s        subsumption elimination
  - -p        pure literal elimination
  - -u        unit literal elimination

 ```sh
$ python main.py ../inputs/classicFormat/valid1.txt
$ python main.py ../inputs/newFormat/invalid1.txt -a
$ python main.py ../inputs/newFormat/invalid1.txt -s -p -u
$ python main.py ../inputs/newFormat/invalid1.txt -s -p
$ ...
```
