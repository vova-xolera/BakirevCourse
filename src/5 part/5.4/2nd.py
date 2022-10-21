l = list(input())
num = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

if len(l) != 16:
    print("Нет")

for i, a in enumerate(l):
    if i == 0 and a != '+':
        print("Нет")
        break
    elif i == 1 and a != "7":
        print("Нет")
        break
    elif i == 2 and a != '(':
        print("Нет")
        break
    elif i == 6 and a != ')':
        print("Нет")
        break
    elif (i == 10 or i == 13) and a != "-":
        print("Нет")
        break
    elif i in [3, 4, 5, 7, 8, 8, 11, 12, 14, 15] and a not in num:
        print("Нет")
        break

else:
    if len(l) != 16:
        print("Нет")
    else:
        print("Да")
