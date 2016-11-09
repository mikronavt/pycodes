import sys
import re

for line in sys.stdin:
    line = line.rstrip()
    p = re.compile(r'\bcat\b')
    m = re.search(p, line)
    if m is not None:
        print(line)