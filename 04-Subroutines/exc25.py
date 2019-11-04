def jestImie(imie, imiona):
    print("Imiona:", end=" ")
    for name in imiona:
        print(name, end=" ")
    print(f'\nImie: {name}')
    print("Rezultat:", end=" ")
    if imie in imiona:
        print('imie jest zawarte w wykazie imion')
    else:
        print('imie nie jest zawarte w wykazie imion')


imiona = ['Janek', 'Ania', 'Wojtek', 'Zosia']
jestImie('Wojtek', imiona)