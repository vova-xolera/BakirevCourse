t = [["Скажи-ка", "дядя", "ведь", "не", "даром"],
    ["Я", "Python", "выучил", "с", "каналом"],
    ["Балакирев", "что", "раздавал?"]]

w = input()

print(t[0].count(w) != 0 or t[1].count(w) != 0 or t[2].count(w) != 0)