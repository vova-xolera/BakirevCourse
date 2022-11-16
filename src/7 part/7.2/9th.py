lst_in = [int(i) for i in input().split()]


def multi(lst):
    return min(lst) * max(lst)


print(multi(lst_in))
