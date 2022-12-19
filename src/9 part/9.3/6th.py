cities = input().split()

c_len = [cities[k] if i > 5 else '-' for k, i in enumerate(map(len, cities))]

print(*c_len)
