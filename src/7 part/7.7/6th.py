N = int(input())

def get_path(N):
    if N == 2:
        return 2
    elif N == 1:
        return 1
    else:
        return get_path(N - 1) + get_path(N - 2)


print(get_path(N))