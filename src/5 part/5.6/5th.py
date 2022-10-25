import sys

# считывание списка из входного потока
s = sys.stdin.readlines()
lst_in = [list(map(int, x.strip().split())) for x in s]

flag = True

for i in range(len(lst_in)):
    for j in range(len(lst_in)):
        if lst_in[i][j] != lst_in[j][i]:
            print("НЕТ")
            break

    else:
        continue
    break
else:
    print("ДА")
