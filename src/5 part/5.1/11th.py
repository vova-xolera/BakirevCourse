acc = []
i = 100
while i < 1000:
    if i % 47 == 43 and i % 3 == 0:
        acc.append(i)
    i += 1
print(*acc)

