n = int(input())
i = 1
output = 1
while i < n:
    i += 1
    output += 1 / i
print(round(output, 3))
