tab = [7, 5, [3, 6, [2]], 7, [1, [2, 3, [4]], 9, 2], 4]


def suma(tablica):
    suma_tablicy = 0
    for i in tablica:
        if isinstance(i, int):
            suma_tablicy += i
        else:
            suma_tablicy += suma(i)
    return suma_tablicy


print(suma(tab))
