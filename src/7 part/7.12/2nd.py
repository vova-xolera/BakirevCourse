from functools import wraps


def decorator(tags = "tg"):
    def decorator_func(func):
        @wraps(func)
        def wrapper(str):
            return f"<{tags}>{func(str)}</{tags}>"
        return wrapper
    return decorator_func


@decorator(tags="div")
def downgrade(str):
    return str.lower()


print(downgrade(input()))
