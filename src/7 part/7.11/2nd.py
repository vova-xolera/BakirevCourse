
def show_menu(func):
    def wrapper(*args):
        list = func(*args)
        for i, k in enumerate(list):
            print(f"{i + 1}. {k}")

    return wrapper


@show_menu
def get_menu(str):
    return [i for i in str.split()]


inp_str = input()

get_menu(inp_str)
