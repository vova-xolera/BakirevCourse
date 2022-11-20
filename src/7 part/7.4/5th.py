def str_min(str1, str2):
   return min(str1, str2)


def str_min3(str1, str2, str3):
    return str_min(str1, str_min(str2, str3))


def str_min4(str1, str2, str3, str4):
    return str_min(str1, str_min3(str2, str3, str4))

print(str_min3("ну", "юга", "да"))
