a = input()

msg = "палиндром" if a.lower() == a.lower()[-1::-1] else "не палиндром"

print(msg)