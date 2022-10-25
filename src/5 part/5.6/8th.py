n = int(input())
coin = [64, 32, 16, 8, 4, 2, 1]

for i in coin:
    while n >= i:
        print(i, end=' ')
        n -= i
