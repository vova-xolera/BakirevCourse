import math

lst = [int(a) for a in input().split()]

ln = int(math.sqrt(len(lst)))

matrix = [[i for i in lst[ln * j: ln * (j + 1)]] for j in range(ln)]

print(matrix)
