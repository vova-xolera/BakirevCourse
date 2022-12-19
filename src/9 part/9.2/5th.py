import math


def prime_numbers(n):
    n = 2
    result = []
    while len(result) != 20:
        for i in range(2, math.floor((n) / 2) + 1):
            if n % i == 0:
                n += 1
                break
        else:
            result.append(n)
            n += 1
    return result


print(*prime_numbers(20))
