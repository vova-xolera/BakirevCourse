a = int(input())

gen = (i ** 3 for i in (abs(j) for j in range(-a, a + 1)))

result = []

for i in range(4):
    result.append(next(gen))

print(*result)
