from statistics import mean

marks = list(map(int, input().split()))
print(round(mean(marks), 1))
