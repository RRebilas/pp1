value = int(input("Podaj kwote w zl: "))
print(f"Kwota {value} zl w monetach: ")
while value > 0:
    print(f"5 zl - {value // 5} szt")
    value -= 5 * (value // 5)
    print(f"2 zl - {value // 2} szt")
    value -= 2 * (value // 2)
    print(f"5 zl - {value // 1} szt")
    value -= 1 * (value // 1)
