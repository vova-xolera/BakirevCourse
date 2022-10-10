p = [0] * 10
acc = 0
while acc != 5:
    n = int(input())
    if p[n] == 1:
        continue
    else:
        p[n] = 1
        acc += 1
print(*p)
