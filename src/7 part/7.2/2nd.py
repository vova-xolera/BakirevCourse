inp_lst = [int(i) for i in input().split()]


def is_triangle(a, b, c):
     return b + c > a and c + a > b and a + b > c


print(is_triangle(*inp_lst[:3]))
