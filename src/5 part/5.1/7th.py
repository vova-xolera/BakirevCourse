x = int(input())
curr = 1
acc = [1]
while x > 1:
    acc.append(curr)
    curr += acc[-2]
    x -= 1
print(*acc)
