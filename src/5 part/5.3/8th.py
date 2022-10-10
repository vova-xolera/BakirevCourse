n = int(input())
b = False
if n == 1:
    b = True
else:
    for x in range(2, n):
        if n % x == 0:
            b = True
if b:
    print("НЕТ")
else:
    print("ДА")
