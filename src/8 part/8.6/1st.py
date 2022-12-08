try:
    with open("abc.txt") as f:
        r = f.read(1)
except FileNotFoundError:
    print("File Not Found")
