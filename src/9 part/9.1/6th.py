cities = ["Москва", "Ульяновск", "Самара", "Уфа", "Омск", "Тула"]

gen = (i for i in cities * int(1000000 / len(cities)))

for i in range(20):
    print(next(gen), end=' ')
