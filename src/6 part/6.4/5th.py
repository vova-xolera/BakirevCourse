lst_in = ['EvgeniyK: спасибо большое!', 'LinaTroshka: лайк и подписка!', 'Sergey Karandeev: крутое видео!', 'Евгений Соснин: обожаю', 'EvgeniyK: это повтор?', 'Sergey Karandeev: нет, это новое видео']

print(len(set(i.split(":")[0] for i in lst_in)))

