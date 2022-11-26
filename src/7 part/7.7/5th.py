d = [1, 2, [True, False], ["Москва", "Уфа", [100, 101], ['True', [-2, -1]]], 7.89]


def get_line_list(d, a=[]):
    for f in d:
        if type(f) == list:
            get_line_list(f, a)
        else:
            a.append(f)
    return a


print(get_line_list(d))
