t_in = tuple(int(i) for i in (input().split()))
t_out = tuple()
for i, n in enumerate(t_in):
    if t_in.count(n) > 1:
        t_out += (i,)
print(*t_out)