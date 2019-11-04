def cyfry_naturalnej(num):
    if num > 0:
        return num % 10 + cyfry_naturalnej(num // 10)
    return 0


print(cyfry_naturalnej(999))