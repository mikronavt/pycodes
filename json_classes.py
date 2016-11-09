import json

json_string = input()

classes_list = json.loads(json_string)

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

for cl in classes_list:
    add_class(cl['name'], *cl['parents'])


parents_count = {}

for c1 in classes:
    for c2 in classes:
        if is_parent(c1,c2):
            parents_count[c1] = parents_count.get(c1, 0) + 1

output_list = []

for cl in parents_count:
    output_list.append(cl + " : " + str(parents_count[cl]))

output_list.sort()

for output_string in output_list:
    print(output_string)