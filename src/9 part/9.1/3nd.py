a, b = map(int, input().split())

for i, n in enumerate((j for j in range(a, b + 1))):
    if i == 5:
        break
    print(abs(n))

