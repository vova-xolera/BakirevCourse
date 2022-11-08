k = {}
while True:
    n = int(input())
    if n == 0:
        break
    if n in k:
        print(f"значение из кэша: {k.get(n)}")
    else:
        n_sqrt = round(n ** 0.5, 2)
        print(n_sqrt)
        k[n] = n_sqrt


