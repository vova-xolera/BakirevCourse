lst = list(input())
lst.remove("+")
lst.remove("7")
lst.insert(0, "8")
lst.remove("-")
lst.remove("-")
print("".join(lst))

