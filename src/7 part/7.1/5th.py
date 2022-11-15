def perimetr(width: int, height: int):
    print(f"Периметр прямоугольника, равен {(width + height) * 2}")


lst_in = [int(i) for i in input().split()]
perimetr(lst_in[0], lst_in[1])