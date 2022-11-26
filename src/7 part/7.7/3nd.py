i = int(input())


def fib_rec(N, f=[]):
    if N == 0:
        return f[:]
    elif len(f) == 0:
        f.append(1)
        f.append(1)
        fib_rec(N - 2, f)
        return f[:]
    else:
        f.append(f[-1] + f[-2])
        fib_rec(N - 1, f)


print(fib_rec(i))
