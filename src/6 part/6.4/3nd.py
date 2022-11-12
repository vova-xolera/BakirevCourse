str = input()
s = set()
for symbol in str:
    if symbol >= '0' and symbol <= '9':
        s.add(symbol)
if len(s) > 0:
    print(*sorted(s))
else:
    print('НЕТ')
