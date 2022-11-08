import sys

# считывание списка из входного потока
s = sys.stdin.readlines()
lst_in = [list(map(int, x.strip().split())) for x in s]

lst = [j for i in lst_in[::-1] for j in i[::-1]]

print(*lst)