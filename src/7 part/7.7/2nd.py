lst_in =[int(i) for i in input().split()]

result = 0


def get_rec_sum(lst, acc=0):

    if acc < len(lst) - 1:
        lst[-1] += lst[acc]
        get_rec_sum(lst, acc + 1)
    return lst[-1]


print(get_rec_sum(lst_in))
