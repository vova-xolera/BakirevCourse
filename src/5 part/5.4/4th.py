a = list(map(int, input().split()))

for i, n in enumerate(a):
    a[i] = n ** 2
print(*a)