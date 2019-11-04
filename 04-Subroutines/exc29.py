def mediana(tablica):
    tablica.sort()
    dl = len(tablica)
    if dl % 2 == 0:
        return (tablica[int(dl / 2)] + tablica[int(dl / 2 - 1)]) / 2
    else:
        return tablica[int((dl - 1) / 2)]


def dominanta(tablica):
    counter = 0
    num = tablica[0]
    for digit in tablica:
        current_counter = tablica.count(digit)
        if current_counter > counter:
            counter = current_counter
            num = digit
    return num


tab = [2, 3, 5, 2, 9, 8, 1, 3, 9, 1, 1, 4, 7, 7, 1, 4]
print(f"Mediana zbioru liczb: {mediana(tab)}")
print(f"Dominanta zbioru liczb: {dominanta(tab)}")
