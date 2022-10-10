import sys

# считывание списка из входного потока
lst_in = list(map(str.strip, sys.stdin.readlines()))

acc = []
l = len(lst_in)
i = 0
while l != i:
    if lst_in[i].find(" ") == -1:
        acc.append(lst_in[i])
    i += 1
print(*acc)
