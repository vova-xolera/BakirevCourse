import sys

# считывание списка из входного потока
lst_in = list(map(str.strip, sys.stdin.readlines()))

tup_out = tuple(zip(*zip(*[x.split() for x in lst_in])))

for i in tup_out:
    print(*i)