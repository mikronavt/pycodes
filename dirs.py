import os

start_path = "C:\\1\\prog\\main\\main"
lst = []
for tup in os.walk(start_path):
    flag = False
    for f in tup[2]:
        if f[-3::] == ".py":
            flag = True
            break
    if flag:
        lst.append(tup[0].replace("C:\\1\\prog\\main\\", ""))

lst.sort()
for p in lst:
    print(p)
