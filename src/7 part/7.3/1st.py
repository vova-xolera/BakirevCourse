def get_nod(a, b):
    if a > b:
        b, a = a, b
    while a != 0:
        b, a = a, b % a
    return b

print(get_nod(100, 15))
