def add_len(str):
    return str, len(str),


d = dict(add_len(i) for i in input().split())

a = sorted(d, key=lambda x: d[x])
print(*a)