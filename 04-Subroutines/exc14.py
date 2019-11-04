def wystepuje(liczba, tablica):
    print(f"Liczba: {liczba}")
    print("Tablica:", end=" ")
    for num in tablica:
        print(num, end=" ")
    print("\nRezultat:", end=" ")
    if liczba in tablica:
        print("Podana liczba wystepuje w tablicy")
    else:
        print("Podana liczba nie wystepuje w tablicy")


liczba = int(input("Podaj liczbe: "))
wystepuje(liczba, [15, 38, 7, 23, 14])
