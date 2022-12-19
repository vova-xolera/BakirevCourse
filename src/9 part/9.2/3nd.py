import random
from string import ascii_lowercase, ascii_uppercase

chars = ascii_lowercase + ascii_uppercase + "0123456789!?@#$*"

# установка зерна датчика случайных чисел (не менять)
random.seed(1)

n = int(input())


def get_pass(n):
    while True:
        passw = ''
        for i in range(n):
            indx = random.randint(0, len(chars) - 1)
            passw += chars[indx]
        yield passw


gen = get_pass(n)

for i in range(5):
    print(next(gen))
