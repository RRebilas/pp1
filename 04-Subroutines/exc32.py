def transpozycja(macierz):
    print("Macierz: ")
    for i in range(3):
        for j in range(3):
            print(macierz[i][j], end=' ')
        print()
    print("Macierz transponowana: ")
    for i in range(3):
        for j in range(3):
            print(macierz[j][i], end=' ')
        print()


macierz = [[1, 2, 0],
           [0, 0, 3],
           [5, 1, 1]]
transpozycja(macierz)
