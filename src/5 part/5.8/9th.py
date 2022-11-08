inp = input().split()

print([[inp[i], int(inp[i + 1])] for i in range(0, len(inp), 2)])
