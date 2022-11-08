import sys

# считывание списка из входного потока
lst_in = list(map(str.strip, sys.stdin.readlines()))

d = {}
for n in lst_in:
    parse_lst = n.split()
    if parse_lst[1] in d:
        val = d.get(parse_lst[1])
        val.append(parse_lst[0])
    else:
        val = [parse_lst[0]]
    d[parse_lst[1]] = val

print(*sorted(d.items()))