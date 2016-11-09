import sys

for line in sys.stdin:
    line = line.rstrip()
    c = line.count("cat")
    if c>=2:
        print(line)