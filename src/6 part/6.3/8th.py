import sys

# считывание списка из входного потока
lst_in = ['Главная home', 'Python learn-python', 'Java learn-java', 'PHP learn-php']


print(tuple(tuple(j) for j in (i.split() for i in lst_in)))