from string import ascii_lowercase

gen = [j + i for j in ascii_lowercase for i in ascii_lowercase]

for i in range(50):
    print(gen[i], end=' ')
