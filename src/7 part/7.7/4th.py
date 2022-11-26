n = int(input())


def fact_rec(N):
    if N == 0:
        return 1
    if N > 0:
        return N * fact_rec(N - 1)
    return N


print(fact_rec(n))
