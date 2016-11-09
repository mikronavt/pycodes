import re
import sys

for line in sys.stdin:
    line = line.rstrip()
    pattern = r"\b(\w)(\w)"
    f = re.sub(pattern, r"\2\1", line)
    print(f)

