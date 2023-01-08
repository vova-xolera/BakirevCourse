a = set(map(int, input().split()))
b = set(int(x) for x in input().split())

c = set(filter(lambda x: x % 2 == 0, (a & b)))

print(*sorted(c))
