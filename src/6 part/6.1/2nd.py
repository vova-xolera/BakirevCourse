
lst_in = ['5=отлично', '4=хорошо', '3=удовлетворительно']
d = {}
for x in lst_in:
     spl_x = x.split('=')
     d[int(spl_x[0])] = spl_x[1]

print(*sorted(d.items()))