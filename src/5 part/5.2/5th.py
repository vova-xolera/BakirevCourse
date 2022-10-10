n = int(input())
acc = []
i = 1
while n != i - 1:
    if i % (5 * 3) == 0:
        acc.append(i)
    i += 1
    if i >= 100:
        print("слишком большое значение n")
        break
else:
    print(*acc)
