a = int(input())
money = 1000
while a:
    money *= 1.05
    a -= 1
print(round(money, 2))
