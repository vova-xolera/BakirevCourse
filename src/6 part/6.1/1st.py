st = input().split()

lst = ([[x if i % 2 == 0 else int(x) for i, x in enumerate(row.split('='))] for row in st])

d = dict(lst)

print(*sorted(d.items()))
