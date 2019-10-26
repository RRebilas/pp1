tries_count = 0
pin_code = '0805'
for i in range(3):
    typed_pin = input("Podaj kod PIN: ")
    if typed_pin == pin_code:
        print("Kod PIN poprawny")
        break
    else:
        print("Kod PIN niepoprawny")
        tries_count += 1
    if tries_count == 3: print("Karta platnicza zostala zablokowana")
