lst_in = input().split()
d = {}
for x in lst_in:
     spl_x = x.split('=')
     d[(spl_x[0])] = spl_x[1]

print("ДА" if 'house' in d and 'True' in d and '5' in d else "НЕТ")