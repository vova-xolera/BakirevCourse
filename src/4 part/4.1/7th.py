x = input().split()

if "Москва" in x:
    x.remove("Москва")

print(*x)
