lst_1 = [float(i) for i in input().split()]
lst_2 = input().split()
lst = [*lst_1, *lst_2]

print(*lst)