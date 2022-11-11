lst_in = tuple(input().lower().split())

t = tuple(x for x in lst_in if "ва" in x)

print(*t)