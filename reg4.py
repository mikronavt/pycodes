import sys
import re

for line in sys.stdin:
    line = line.rstrip()
    p = re.compile("human")
    m = re.sub(p, "computer", line)
    print(m)