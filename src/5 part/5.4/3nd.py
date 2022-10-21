l = input().replace(' ', '')
list_of_numbers = []
w_acc = ""
plus_and_minus = ["+", "-"]
for i in range(len(l)):
    if l[i] not in plus_and_minus:
        w_acc += l[i]
    else:
        list_of_numbers.append(w_acc)
        list_of_numbers.append(l[i])
        w_acc = ''
list_of_numbers.append(w_acc)

result = int(list_of_numbers[0])
for i, n in enumerate(list_of_numbers):
    if n == '+':
        result = result + int(list_of_numbers[i + 1])
    if n == '-':
        result = result - int(list_of_numbers[i + 1])
print(result)
