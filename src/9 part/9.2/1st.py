N = int(input())


def get_sum(N):
    for i in range(N + 1):
        yield sum(range(i))

