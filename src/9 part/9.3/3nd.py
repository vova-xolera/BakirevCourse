import sys

# считывание списка из входного потока
lst_in = list(map(str.strip, sys.stdin.readlines()))

lst2D = []

for i in lst_in:
    lst2D.append(list(map(int, i.split())))

print(lst2D)
