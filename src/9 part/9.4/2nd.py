import sys

# считывание списка из входного потока
lst_in = ['зонт=1000', 'палатка=10000', 'спички=22', 'котелок=543']

tuple_in = tuple(map(tuple, [x.split('=') for x in lst_in]))


lst_out = list(filter(lambda a: int(a[1]) >= 500, tuple_in))

print(*[x[0] for x in lst_out])
