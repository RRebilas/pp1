def suma(tablica, i):
    if i > 0:
        return tablica[i] + tablica[i - 1]

tab = [7, 5, [3, 6, [2]], 7, [1, [2, 3, [4]], 9, 2], 4]
tab1 = [1, 2, 3, 4, 5, 6]
print(suma(tab1, len(tab1) - 1))