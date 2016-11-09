s = input()
a = input()
b = input()

if (a in b) and (s.find(a) >= 0):
    print("Impossible")
else:
    #lst = []
    counter = 0
    while True:
        if s.find(a) < 0:
            print(counter)
            break
        else:
            #lst.append(s)
            s = s.replace(a,b)
            counter += 1
        #if s in lst:
        #    print("Impossible")