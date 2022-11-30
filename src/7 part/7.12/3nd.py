from functools import wraps

t = {'ё': 'yo', 'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e', 'ж': 'zh',
     'з': 'z', 'и': 'i', 'й': 'y', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o', 'п': 'p',
     'р': 'r', 'с': 's', 'т': 't', 'у': 'u', 'ф': 'f', 'х': 'h', 'ц': 'c', 'ч': 'ch', 'ш': 'sh',
     'щ': 'shch', 'ъ': '', 'ы': 'y', 'ь': '', 'э': 'e', 'ю': 'yu', 'я': 'ya'}


def decorator(chars = '?!'):
    def decorator_func(func):
        @wraps(func)
        def wrapper(str):
            for i, s in enumerate(str):
                if s in chars:
                    str = str.replace(s, '-')
            while '--' in str:
                str = str.replace('--', '-')
            return func(str)
        return wrapper
    return decorator_func


@decorator(chars="?!:;,. ")
def replaser(str):
    result = ''
    str = str.lower()
    for i, s in enumerate(str):
        if s in t.keys():
            result += t.get(s)
        else:
            result += s
    return result


print(replaser(input()))

