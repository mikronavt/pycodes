objects = [1, 2, 1, 2, 3]

unique = set()

for o in objects:
    unique.add(id(o))

print(len(unique))