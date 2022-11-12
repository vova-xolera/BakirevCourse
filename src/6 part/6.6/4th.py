str = input().lower()
d = {i: str.count(i) for i in str.split()}
print(d.get('и', 0))
