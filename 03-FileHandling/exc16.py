import re
komunikat = 'wtorek - 23C, środa - 17C, czwartek 25C'
cyfry = re.findall('\d{2}',komunikat)
suma = 0
for i in cyfry:
    suma += int(i)
print(f"Srednia prognozowana pogoda wynosi: {int(suma/len(cyfry))}")