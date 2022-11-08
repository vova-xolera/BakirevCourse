inp = input().split()

lst_city = [x for i, x in enumerate(inp) if i % 2 == 0]
lst_pop = [int(x) for i, x in enumerate(inp) if i % 2 == 1]
lst = []

for i in range(len(lst_city)):
    pare = [lst_city[i], lst_pop[i]]
    lst.append(pare)

print(lst)