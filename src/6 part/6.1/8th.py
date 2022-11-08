lst_in = ['ustanovka-i-zapusk-yazyka', 'ustanovka-i-poryadok-raboty-pycharm', 'peremennyye-operator-prisvaivaniya-tipy-dannykh', 'arifmeticheskiye-operatsii', 'ustanovka-i-poryadok-raboty-pycharm']

k = []

for i, n in enumerate(lst_in):
    if n in k:
        print(f"Взято из кэша: HTML-страница для адреса {n}")
    else:
        print(f"HTML-страница для адреса {n}")
        k.append(n)

