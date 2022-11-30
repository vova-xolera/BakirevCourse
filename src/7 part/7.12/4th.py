from functools import wraps


def decorator(func):
    @wraps(func)
    def wrapper(s):
        lst = func(s)
        return sum(lst)

    return wrapper



@decorator
def get_list(s):
    """Функция для формирования списка целых значений"""
    return [int(i) for i in s.split()]


print(get_list(input()))
