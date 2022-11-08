lst_in = input().split()

d = {}
for n in lst_in:
    if n[:2] in d:
        val = d.get(n[:2])
        val.append(n)
    else:
        val = [n]
    d[n[:2]] = val

print(*sorted(d.items()))