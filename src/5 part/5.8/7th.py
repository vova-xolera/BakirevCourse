lst = [float(x) for x in input().split()]

print(*[x for i, x in enumerate(lst) if i % 2 == 0])
