st = input()
it = iter(st)
while True:
    n = next(it)
    if n != " ":
        print(n, end='')
    else:
        break
