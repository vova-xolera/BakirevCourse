import math

lst = [x for x in input().split()]

z = zip(lst[::3], lst[1::3], lst[2::3])
[print(*i) for i in z]

