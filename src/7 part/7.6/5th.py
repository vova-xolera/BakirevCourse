import sys

# считывание списка из входного потока
lst_in = ['Города=about-cities', 'Машины=read-of-cars', 'Самолеты=airplanes']

d = dict([i.split('=') for i in lst_in])

menu = {'Главная': 'home', 'Архив': 'archive', 'Новости': 'news'}

menu = {**menu, **d}
