N = int(input())


def get_sum(N):
    a = b = c = 1
    for _ in range(N):
        yield a
        a, b, c = b, c, a + b + c


print(*get_sum(N))
