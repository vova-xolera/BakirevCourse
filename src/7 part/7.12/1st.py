from functools import wraps

str = input()


def decorator(start):
    def decorator_func(func):
        @wraps(func)
        def wrapper(str):
            return start + func(str)
        return wrapper
    return decorator_func


@decorator(start=5)
def summer(str):
    lst = [int(i) for i in str.split()]
    return sum(lst)


print(summer(str))
