inp_lst = input().split()


def checker(x):
     if not ('@' in x and '.' in x and x.index('@') < x.index('.')):
          return False
     for i in x:
          if not (i.isalpha() or i.isdigit() or i in ['_', '.', '@']):
               return False
     return True


print(*list(filter(checker, inp_lst)))
