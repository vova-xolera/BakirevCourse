import math
x = int(input())
acc = 1
while x:
    acc = acc * (x % 10)
    x = math.floor(x / 10)
print(acc)
