a, b = map(int, input().split())


def f(x):
    return round(0.5 * pow(x, 2) - 2.0, 2)


def new_range(a, b, c):
    result = []
    while a < b:
        result.append(a)
        a += c
    return result


gen = (f(x) for x in new_range(a, b, 0.01))

for i in range(20):
    print(next(gen), end=' ')
