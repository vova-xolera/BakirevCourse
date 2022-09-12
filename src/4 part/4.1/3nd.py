a, b = map(int, input().split())

if a % b == 0:
    print(int(a / b))
else:
    print(f"{a} на {b} нацело не делится")

