lst = list(map(float, input().split()))

for i, value in enumerate(lst):
    if value < 0:
        lst[i] = -1.0

print(*lst)