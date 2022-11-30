def get_sq(width, height):
    return width * height


def func_show(func):
    def wrapper(*args):
        result = func(*args)
        print(f"Площадь прямоугольника: {result}")

    return wrapper


lst_in = [int(i) for i in input().split()]


get_sq = func_show(get_sq)


get_sq(lst_in[0], lst_in[1])

