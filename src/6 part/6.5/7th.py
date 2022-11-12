N = int(input())
s = set()
s1 = {2, 3, 5}
while True:
    if N % 7 == 0:
        s.add(7)
        N /= 7
    elif N % 5 == 0:
        s.add(5)
        N /= 5
    elif N % 3 == 0:
        s.add(3)
        N /= 3
    elif N % 2 == 0:
        s.add(2)
        N /= 2
    else:
        break
print('ДА' if s1 <= s else 'НЕТ')
