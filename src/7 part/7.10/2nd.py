def counter_add(n):
    def step(a):
        nonlocal n
        return a + n
    return step


cnt = counter_add(2)

k = int(input())

print(cnt(k))
