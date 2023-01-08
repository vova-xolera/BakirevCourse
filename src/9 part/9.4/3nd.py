lst_in = map(int, input().split())

print(*list(filter(lambda x: 9 < abs(x) < 100, lst_in)))
