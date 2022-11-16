def checker(n):
    return n % 2


lst = [int(i) for i in input().split() if checker(int(i))]

print(*lst)