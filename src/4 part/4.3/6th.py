a, b, c = map(int, input().split())

m = ['до', 'ре', 'ми', 'фа', 'соль', 'ля', 'си']

first = m[a - 1] if (a != 1 and a != 4) else ("#" + m[a - 1])
second = m[b - 1] if (b != 1 and b != 4) else ("#" + m[b - 1])
third = m[c - 1] if (c != 1 and c != 4) else ("#" + m[c - 1])

print(f"{first} {second} {third}")
