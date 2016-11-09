import re
import sys

for line in sys.stdin:
    line = line.rstrip()
    pattern = r"\b((\w+)\2)\b"
    duplicates = re.search(pattern, line)
    if duplicates is not None:
        print(line)