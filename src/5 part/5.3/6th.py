l = list(input().split())
acc = []
for x in range(len(l)):
    acc.append(len(l[x]))
print(*acc)
