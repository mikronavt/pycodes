import re
import sys

for line in sys.stdin:
    line = line.rstrip()
    pattern = r"((\w)\2+)"
    f = re.sub(pattern, r"\2", line)
    print(f)

