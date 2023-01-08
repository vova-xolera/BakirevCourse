lst_in = input().split()

iter_out = filter(lambda x: len(x) > 5, lst_in)

print(next(iter_out), end=' ')
print(next(iter_out), end=' ')
print(next(iter_out), end='')
