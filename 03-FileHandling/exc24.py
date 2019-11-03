two_dimensional = [['Marek', 'Zelnik', 'zelnik@sed.pl'], ['Ewa', 'Maj', 'maje@wp.pl'],
                   ['Piotr', 'Wyga', 'wygap@gop.pl']]
with open("data.csv", 'w') as file:
    file.write('Imie,Nazwisko,Email\n')
    for data in two_dimensional:
        for single_data in data:
            file.write(single_data)
            if single_data == data[2]:
                file.write('\n')
            else:
                file.write(',')
