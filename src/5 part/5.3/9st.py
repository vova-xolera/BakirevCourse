lst = [city.rstrip("ьъы") for city in input().split()]
for i in range(1,len(lst)):
    if lst[i-1][-1] != lst[i][0].lower():
        print("НЕТ")
        break
else:
    print("ДА")