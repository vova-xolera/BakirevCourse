a = float(input())
N = 10
output = []
i = 1
while i < N:
    i += 1
    output.append(round(a * i, 1))
print(*output)
