def decorator(func):
    def wrapper(*args):
        couple = func(*args)
        lst1 = couple[0]
        lst2 = couple[1]
        d = dict()
        for i, k in enumerate(lst1):
            d[k] = lst2[i]
        return d

    return wrapper

@decorator
def reader(str1, str2):
    lst1 = [i for i in str1.split()]
    lst2 = [i for i in str2.split()]
    return lst1, lst2


d = reader(input(), input())
print(*sorted(d.items()))
