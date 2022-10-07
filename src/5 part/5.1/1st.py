x, y = map(int, input().split())
output = []
while x < y + 1:
    output.append(x**2)
    x += 1
print(*output)
