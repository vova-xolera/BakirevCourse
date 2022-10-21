s = input()
acc = []
while s.find("ра") != -1:
    acc.append(s.find("ра"))
    s = s.replace("ра", "цц", 1)
if acc == []:
    print(-1)
else:
    print(*acc)