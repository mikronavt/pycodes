import sys
import re

for line in sys.stdin:
    line = line.rstrip()
    p = re.compile(r"\b[aA]+\b")
    m = re.sub(p, "argh", line, count=1)
    print(m)