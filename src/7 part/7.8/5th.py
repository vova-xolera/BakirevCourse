def filter_lst(it, key=None):
    if key is None:
        return tuple(it)

    res = ()
    for x in it:
        if key(x):
            res += (x,)

    return res

lst = [int(i) for i in input().split()]

print(*filter_lst(lst))
print(*filter_lst(lst, lambda a: a < 0))
print(*filter_lst(lst, lambda a: a >= 0))
print(*filter_lst(lst, lambda a: 3 <= a <= 5))
