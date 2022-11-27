def tegger(s):
    def inner():
        nonlocal s
        s = f"<h1>{s}</h1>"
        return s
    return inner


print(tegger(input())())
