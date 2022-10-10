st = input().split()
i = len(st)
while i:
    if len(st[i - 1]) <= 5:
        print("НЕТ")
        break
    i -= 1
else:
    print("ДА")
