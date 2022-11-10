things = {'карандаш': 20, 'зеркальце': 100, 'зонт': 500, 'рубашка': 300, 
          'брюки': 1000, 'бумага': 200, 'молоток': 600, 'пила': 400, 'удочка': 1200,
          'расческа': 40, 'котелок': 820, 'палатка': 5240, 'брезент': 2130, 'спички': 10}

N = int(input()) * 1000

value_list = sorted(things.values())[::-1]

result = []

for n in value_list:
    if N - n >= 0:
        N -= n
        key = ''
        for k, v in things.items():
            if v == n:
                result.append(k)
                break

print(*result)
