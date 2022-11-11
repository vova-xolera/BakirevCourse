t = ((1, 0, 0, 0, 0),
     (0, 1, 0, 0, 0),
     (0, 0, 1, 0, 0),
     (0, 0, 0, 1, 0),
     (0, 0, 0, 0, 1))

N = int(input())

t1 = ()

for i in range(N):
    t1 += t[i][:N],

for i in t1:
    print(*i)
