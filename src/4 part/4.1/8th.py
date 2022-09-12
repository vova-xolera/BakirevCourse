a, b, c, d = map(int, input().split())

c += 2
d += 2
if a >= c and b >= d or a >= d and b >= c:
    print("ДА")
else:
    print("НЕТ")
