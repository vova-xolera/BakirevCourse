m = '''1. Введение в Python
2. Строки и списки
3. Условные операторы
4. Циклы
5. Словари, кортежи и множества
6. Выход'''

lst = m.split('\n')

inp = int(input())

if  inp == 1:
    print(lst[0])
elif inp == 2:
    print(lst[inp - 1])
elif inp == 3:
    print(lst[inp - 1])
elif inp == 4:
    print(lst[inp - 1])
elif inp == 5:
    print(lst[inp - 1])
elif inp == 6:
    print(lst[inp - 1])
