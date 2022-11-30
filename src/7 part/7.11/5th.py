t = {'ё': 'yo', 'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e', 'ж': 'zh',
     'з': 'z', 'и': 'i', 'й': 'y', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o', 'п': 'p',
     'р': 'r', 'с': 's', 'т': 't', 'у': 'u', 'ф': 'f', 'х': 'h', 'ц': 'c', 'ч': 'ch', 'ш': 'sh',
     'щ': 'shch', 'ъ': '', 'ы': 'y', 'ь': '', 'э': 'e', 'ю': 'yu', 'я': 'ya'}


def decorator(func):
     def wrapper(str2):
          s = func(str2)
          while '--' in s:
               s = s.replace('--', '-')
          return s
     return wrapper


@decorator
def changer(str1):
     result = ""
     for i in str1.lower():
          if i in t.keys():
               result += t.get(i)
          elif i in ": ;.,_":
               result += '-'
          else:
               result += i
     return result


s = input()

print(changer(s))
