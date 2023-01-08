a = map(int, input().split())
b = map(int, input().split())
c = map(lambda x: x[0] * x[1], zip(a, b))
print(next(c), next(c), next(c))
