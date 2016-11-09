import itertools

def primes():
    i = 2
    while True:
        flag = True
        for c in range(2,int(i**0.5) + 1):
            if i%c == 0:
                flag = False
                break
        if flag:
            yield i
        i += 1


print(list(itertools.takewhile(lambda x : x <= 31, primes())))