st = input().split()
i = len(st)
while i:
    if st[i - 1][0].lower() == st[i - 1][-1].lower():
        print("ДА")
        break
    i -= 1
else:
    print("НЕТ")
