def outer(tp):
    def inner(str):
        nonlocal tp
        if tp == "list":
            return [int(i) for i in str.split()]
        else:
            return tuple(int(i) for i in str.split())

    return inner

typ = input()

lst = input()

cnt = outer(typ)

print(cnt(lst))
