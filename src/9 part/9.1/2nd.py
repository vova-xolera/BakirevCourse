# ввод значений a и b (переменные a и b не менять!)
a, b = map(int, input().split())

tp = tuple((i ** 2 for i in range(a, b + 1)))

print(tp)
