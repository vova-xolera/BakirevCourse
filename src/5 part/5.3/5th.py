l = list(map(int, input().split()))
s = 0
for x in range(len(l)):
    if l[x] % 2 != 0:
        s += l[x]
print(s)
