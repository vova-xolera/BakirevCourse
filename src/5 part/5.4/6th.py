l = list(map(float, input().split()))
result = l[0]
for n in l:
    if result > n:
        result = n
print(result)
