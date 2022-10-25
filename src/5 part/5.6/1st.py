N = int(input())
for i in range(N):
    for j in range(N):
        if j == N - 1:
            print(5)
        else:
            print(1, end=' ')
