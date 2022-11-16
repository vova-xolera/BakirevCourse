def is_large(str):
    return len(str) >= 6


lst = [i for i in input().split() if is_large(i)]

print(*lst)
