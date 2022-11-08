N = int(input())

lst = [[1 if a == b else 0 for a in range(N)] for b in range(N)]

for i in lst:
    print(*i)
