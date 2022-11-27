def counter_add():

    def step(a):
        return a + 5
    return step

cnt = counter_add()

k = int(input())

print(cnt(k))
