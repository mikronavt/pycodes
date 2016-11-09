s = input()
t = input()

counter = 0
for i in range(len(s)):
    if s[i::].startswith(t):
        counter += 1

print(counter)