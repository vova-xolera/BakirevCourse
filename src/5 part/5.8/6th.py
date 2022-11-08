N = int(input())

lst = [[b for a in range(N)] for b in range(N)]
for i in lst:
    print(*i)
