t = tuple(input().split())
t = t + ("Москва",) if 'Москва' not in t else t
print(*t)