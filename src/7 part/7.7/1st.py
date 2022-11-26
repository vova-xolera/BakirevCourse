N = int(input())

def get_rec_N(Num, acc = 1):
    if Num >= acc:
        print(acc)
        get_rec_N(Num, acc+1)

get_rec_N(N)

