lst = [i for i in input().split()]
d = {int(lst[0]) + i: n for i, n in enumerate(lst[1:])}
print(d.get(4))
