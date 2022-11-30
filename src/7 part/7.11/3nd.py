def decorator(func):
    def wrapper(lst):
        return sorted(func(lst))

    return wrapper

@decorator
def get_list(str):
    return [int(i) for i in str.split()]


lst = get_list(input())


print(*lst)
