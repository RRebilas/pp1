def suma(tablica):
    array_sum = 0
    print("Zawartosc tablicy =", end=" ")
    for num in tablica:
        array_sum += num
        print(f"{num}", end=", ")
    print(f"\nsuma = {array_sum}")


suma([2, 3, 4, 5, 6, 6])
