def checker(n):
     return n % 2


while True:
     num = int(input())
     if num == 1:
          break
     if not checker(num):
          print(num)
