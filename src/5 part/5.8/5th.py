N = int(input())

print(*[x for x in range(1, N + 1) if N % x == 0])
