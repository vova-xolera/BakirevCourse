from string import ascii_lowercase, ascii_uppercase
import random
random.seed(1)

N = int(input())
chars = ascii_lowercase + ascii_uppercase


def pass_creator(N):
    while True:
        pas = ''
        for i in range(N):
            indx = random.randint(0, len(chars) - 1)
            pas += chars[indx]
        pas += '@mail.ru'
        yield pas


for i in range(5):
    print(next(pass_creator(N)))
