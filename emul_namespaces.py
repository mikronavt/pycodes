global_namespaces = {'parent':None, 'ns_name':'global'}

def find(name, dict):
    if name == dict['ns_name']:
        return dict
    if dict.get(name,None) is not None:
        return dict[name]
    else:
        for (key, obj) in dict.items():
            if key != 'parent' and type(obj) == type({}):
                ns = find(name, obj)
                if ns is not None:
                    return ns
    return None

def find_ns(name):
    return find(name, global_namespaces)

def create(namespace, parent):
    parent_ns = find_ns(parent)
    if parent_ns is not None:
        parent_ns[namespace] = {'parent':parent, 'ns_name':namespace}

def add(namespace, var):
    ns = find_ns(namespace)
    if ns is not None:
        ns[var] = var

def get(namespace, var):
    ns = find_ns(namespace)
    if ns is not None:
        v = ns.get(var, None)
        if v is not None:
            return ns['ns_name']
        else:
            ns_name = get(ns['parent'], var)
            if ns_name is not None:
                return ns_name
    return None

def command_parser(lst):
    if lst[0] == 'create':
        create(lst[1],lst[2])
    elif lst[0] == 'add':
        add(lst[1],lst[2])
    elif lst[0] == 'get':
        print(get(lst[1],lst[2]))


n = int(input())
for i in range(n):
    lst = input().split()
    command_parser(lst)



