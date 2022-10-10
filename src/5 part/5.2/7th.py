n = int(input())
i = 10
d = 1
while True:
    if i > n:
        print(d)
        break
    i *= 1.1
    d += 1
