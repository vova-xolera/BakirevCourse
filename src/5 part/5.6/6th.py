l = list(map(int, input().split()))
result = []
while len(l) != 0:
    result.append(min(l))
    l.remove(min(l))
print(*result)
