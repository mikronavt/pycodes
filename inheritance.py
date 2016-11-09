classes = {}

def add_class(name, *parents):
    classes[name] = parents

def is_parent(class1, class2):
    if class1 == class2:
        return True
    parents = classes.get(class2, [])
    for c in parents:
        if c == class1:
            return True
    for c in parents:
        if is_parent(class1, c):
            return True
    return False


n = int(input())
for i in range(n):
    values = input().split(':')
    c = values[0].strip()
    if len(values) > 1:
        par = values[1].strip()
        parents = par.split()
    else:
        parents = []
    add_class(c, *parents)



q = int(input())
for i in range(q):
    c1, c2 = input().strip().split()
    print(["No", "Yes"][is_parent(c1,c2)])