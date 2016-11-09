f = open("C:\\1\\prog\\dataset_24465_4.txt", "r")
wf = open("C:\\1\\prog\\result.txt", "w")

a = []

for l in f:
    a.append(l)

a = a[::-1]

for l in a:
    wf.write(l)

wf.close()