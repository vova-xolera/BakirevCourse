lst = list(map(int, input().split()))
x = lst.pop(-1)
lst.append(x % 2 == 1)
print(*lst)
