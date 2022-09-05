a = input()
b = input()
c = input()
d = float(input())

book = [a, b, c, d]
del book[2]
book[1] = "Пушкин"
book[2] = book[2] * 2
print(book)
