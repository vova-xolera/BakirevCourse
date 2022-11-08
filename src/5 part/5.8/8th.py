lst_1 = [int(x) for x in input().split()]
lst_2 = [int(x) for x in input().split()]
result = []

for i in range(len(lst_1)):
    result.append(lst_1[i] + lst_2[i])

print(*result)
