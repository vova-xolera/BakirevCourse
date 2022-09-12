import math

a, b, c = map(int, input().split())

if math.pow(c, 2) == math.pow(a, 2) + b**2:
    print("ДА")
else:
    print('НЕТ')


