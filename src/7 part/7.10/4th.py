def tegger(h):
    def inner(s):
        nonlocal h
        s = f"<{h}>{s}</{h}>"
        return s
    return inner


print(tegger(input())(input()))
