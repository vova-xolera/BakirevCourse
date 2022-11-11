t_in = tuple(int(i) for i in (input().split()))
t_out = tuple()
for n in t_in:
    if n not in t_out:
        t_out += (n,)
print(*t_out)