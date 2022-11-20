def get_biggest_city(*args):
     word = ''
     l_word = 0
     for i in args:
          if len(i) > l_word:
               word = i
               l_word = len(i)
     return word

print(get_biggest_city(""))