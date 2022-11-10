lst_in = input().split()
d = {}
for x in lst_in:
     spl_x = x.split('=')
     d[(spl_x[0])] = spl_x[1]

d.pop('3', '')
d.pop('False', '')
print(*sorted(d.items()))