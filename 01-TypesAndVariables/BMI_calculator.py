height = float(input("Podaj wzrost w cm: "))
weight = int(input("Podaj wagę w kg: "))
bmi = weight / (height / 100) ** 2
msg = "waga prawidłowa" if 18.5 <= bmi <= 25 else "waga nieprawidłowa"
print(f"Twoje bmi to: " + "{:.2f}".format(bmi) + f" - {msg}")
