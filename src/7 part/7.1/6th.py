emale = input().lower()


def symbols(check_emale):
    result = True
    for i in check_emale:
        if not (('a' <= i <= 'z') or ('0' <= i <= '9') or i == '_' or i == '.' or i == '@'):
            result = False
    return result


print("ДА" if symbols(emale) and emale.count('.') > 0 and emale.count('@') else 'НЕТ')

